import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
domain = sys.argv[2]
# date_range = "oneeighty" 
# domain = "ru-clip.net"

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_widgets_for_one_domain_for_all_campaigns/{date_range}_{domain}_p_widgets_for_one_domain_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)

metadata = json_file["metadata"]
data = json_file["data"]

widgets = []
for widget in data.values():
    widgets.append(widget)

df = pd.DataFrame(widgets)

df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)

c1 = df["classification"] == sys.argv[3]
result1 = df[c1]

c2 = df["global_status"] == sys.argv[4]
result2 = df[c2]

c3 = df["cost"] >= float(sys.argv[5])
result3 = df[c3]

c4 = df["profit"] <= -1 * float(sys.argv[6])
result4 = df[c4]

conditions_args = [sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]
conditions_dfs = [result1, result2, result3, result4]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["clicks", "cost", "leads", "revenue", "sales", "widget_id", "cpc",
    "epc", "cpl", "epl", "cps", "eps", "lead_cvr",
    "profit", "global_status", "classification", "domain"])

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

# add a summary row at the top
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["widget_id"] = "summary"
    summary["cpc"] = round(summary["cost"] / summary["clicks"], 2)
    summary["epc"] = round(summary["revenue"] / summary["clicks"], 2)
    summary["classification"] = "NA"
    summary["global_status"] = "NA"
    if summary["clicks"] == 0:
        summary["lead_cvr"] = 0
    else:
        summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
        2)
    rows_with_leads = final_result[final_result["leads"] >= 1]
    number_of_rows_with_leads = len(rows_with_leads.index)
    if number_of_rows_with_leads > 0:
        summary["cpl"] = round(summary["cost"] / summary["leads"], 2)
        summary["epl"] = round(summary["revenue"] / summary["leads"], 2)
    else:
        summary["cpl"] = 0 
        summary["epl"] = 0
    rows_with_sales = final_result[final_result["sales"] >= 1]
    number_of_rows_with_sales = len(rows_with_sales.index)
    if number_of_rows_with_sales > 0:
        summary["cps"] = round(summary["cost"] / summary["sales"], 2)
        summary["eps"] = round(summary["revenue"] / summary["sales"], 2)
    else:
        summary["cps"] = 0
        summary["eps"] = 0
    # Append summary onto the top
    final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
    final_result = final_result.replace(np.nan, "")


json_final_result = json.dumps(final_result[["clicks", "cost", "leads", "revenue", "sales", "widget_id", "cpc",
    "epc", "cpl", "epl", "cps", "eps", "lead_cvr",
    "profit", "global_status", "classification", "domain"]].to_dict("records"))

print(json_final_result)
