import sys
import json
import pandas as pd
import numpy as np

p_widget_id = sys.argv[1]
date_range = sys.argv[2]

with open(f'/home/bsh/Documents/UlanMedia/data/c_widgets_for_one_p_widget/{p_widget_id}_{date_range}_c_widgets_for_one_p_widget_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

# The json data is a dictionary with each widget id as a key and each widget as
# a value. The loop below simple takes the values and puts them into a list. 
widgets = []
for widget in data.values():
    widgets.append(widget)

df = pd.DataFrame(widgets)

if len(df.index) == 0:
    print(json.dumps({}))
    sys.exit()


df["cost"] = round(df["cost"], 2)
df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)

# widget lost more than x times max_lead_cpa
# This is the precondition for every report
# df = df[df["profit"] < -1 * float(sys.argv[3]) * df["max_lead_cpa"]]
df = df[df["profit"] < -1 * 0 * df["max_lead_cpa"]]


# filter on widget status
# This is the precondition2 for every report
status = sys.argv[4]
if status != "all":
    df = df[df["status"] == sys.argv[4]]

# leads >= 1
c1 = df["leads"] >= 1
result1 = df[c1]

# sales >= 1
c2 = df["sales"] >= 1
result2 = df[c2]

conditions_args = [sys.argv[5], sys.argv[6]]
# conditions_args = ["true", "true"]
conditions_dfs = [result1, result2]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]
            )
if final_result is None:
    final_result = df


final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

# add a summary row at the bottom
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["widget_id"] = "summary"
    rows_with_leads = final_result[final_result["leads"] >= 1]
    number_of_rows_with_leads = len(rows_with_leads.index)
    if number_of_rows_with_leads > 0:
        summary["lead_cpa"] = round(summary["cost"] / summary["leads"], 2)
    else:
        summary["lead_cpa"] = 0 
    rows_with_sales = final_result[final_result["sales"] >= 1]
    number_of_rows_with_sales = len(rows_with_sales.index)
    if number_of_rows_with_sales > 0:
        summary["sale_cpa"] = round(summary["cost"] / summary["sales"], 2)
    else:
        summary["sale_cpa"] = 0
    final_result = final_result.append(summary, ignore_index=True)
    final_result = final_result.replace(np.nan, "")


json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]].to_dict("records"))

print(json_final_result)
