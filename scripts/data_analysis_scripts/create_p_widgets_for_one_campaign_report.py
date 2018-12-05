import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
volid = sys.argv[2]

with open(f'/home/bsh/Documents/UlanMedia/data/p_widgets_for_one_campaign/{volid}_{date_range}_p_widgets_for_one_campaign_dataset.json', 'r') as file:
     data = json.load(file)

# The json data is a dictionary with each widget id as a key and each widget as
# a value. The loop below simple takes the values and puts them into a list. 
widgets = []
for widget in data.values():
    widgets.append(widget)
    # the referrer column of each widget is a list of refferers. I am not sure
    # how to best handle lists inside of data frames so, for now, I am just 
    # going to concatenate them into a space separated string. 
    referrers = ""
    for referrer in widget["referrer"]:
        if referrers == "":
            referrers = referrer
        else:
            referrers = f"{referrers} {referrer}"
    widget["referrer"] = referrers

df = pd.DataFrame(widgets)

df["cost"] = round(df["cost"], 2)
df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)

# widget lost more than x times max_lead_cpa
# This is the precondition for every report
df = df[df["profit"] < -1 * float(sys.argv[3]) * df["max_lead_cpa"]]

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
conditions_dfs = [result1, result2]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]].to_dict("records"))

print(json_final_result)
