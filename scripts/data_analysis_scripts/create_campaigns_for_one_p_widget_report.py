import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
widget_id = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_one_p_widget/{widget_id}_{date_range}_campaigns_for_one_p_widget_dataset.json', 'r') as file:
     json_file = json.load(file)

campaigns = json_file["data"]

df = pd.DataFrame(campaigns)

# this condition handles the case where the parent widget dataset is empty.
# The first time I noticed this possibility was when mike excluded a widget
# from all campaigns. The next day, when the app created a dataset for
# campaigns_for_one_parent/child_widget, that dataset was empty. 
if len(df.index) == 0:
    print(json.dumps(campaigns))
    sys.exit()

df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cost"] = round(df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)

# status conditions (all, included, excluded)
c1 = df["status"] == sys.argv[3]
result1 = df[c1]

# widget cost is more than xxx
c2 = df["cost"] > float(sys.argv[4])
result2 = df[c2]

# widget lost more than xxx
c3 = df["profit"] < -1 * float(sys.argv[5])
result3 = df[c3]

conditions_args = [sys.argv[6], sys.argv[7], sys.argv[8]]
conditions_dfs = [result1, result2, result3]


final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
            "cpc", "epc", "mpc", "cpl", "epl", "mpl", "lead_cpa", "lead_cvr",
            "cps", "eps", "mps", "sale_cpa", "profit", "status",
            "classification"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("name", ascending=True)

# add a summary row at the top
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["name"] = "summary"
    summary["mpc"] = ""
    summary["mpl"] = ""
    summary["mps"] = ""
    if summary["clicks"] == 0:
        summary["lead_cvr"] = 0
    else:
        summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
        2)
    rows_with_leads = final_result[final_result["leads"] >= 1]
    number_of_rows_with_leads = len(rows_with_leads.index)
    if number_of_rows_with_leads > 0:
        summary["cpl"] = round(summary["cost"] / summary["leads"], 2)
    else:
        summary["cpl"] = 0 
    rows_with_sales = final_result[final_result["sales"] >= 1]
    number_of_rows_with_sales = len(rows_with_sales.index)
    if number_of_rows_with_sales > 0:
        summary["cps"] = round(summary["cost"] / summary["sales"], 2)
    else:
        summary["cps"] = 0
    # Append summary onto the top
    final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result], sort=True)
    final_result = final_result.replace(np.nan, "")

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
            "cpc", "epc", "mpc", "cpl", "epl", "mpl", "lead_cpa", "lead_cvr",
            "cps", "eps", "mps", "sale_cpa", "profit", "status",
            "classification"]].to_dict("records"))

print(json_final_result)
