import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
#date_range = "seven"
widget_id = sys.argv[2]
#widget_id = "5718588"

with open(f'/home/bsh/Documents/UlanMedia/data/by_child_widgets_data/{widget_id}_{date_range}_by_child_widgets_data.json', 'r') as file:
     data = json.load(file)

# The json data is a dictionary with each voluum id as a key and each widget
# for that campaign as
# a value. The loop below simple takes the values and puts them into a list. 
campaigns = []
for campaign in data.values():
    campaigns.append(campaign)
    # the referrer column of each widget is a list of refferers. I am not sure
    # how to best handle lists inside of data frames so, for now, I am just 
    # going to concatenate them into a space separated string. 
    referrers = ""
    for referrer in campaign["referrer"]:
        if referrers == "":
            referrers = referrer
        else:
            referrers = f"{referrers} {referrer}"
    campaign["referrer"] = referrers

df = pd.DataFrame(campaigns)

df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)

# cost greater than x 
df = df[df["cost"] > float(sys.argv[3])]
#df = df[df["cost"] > 5]

# leads >= 1
c1 = df["leads"] >= 1
result1 = df[c1]

# sales >= 1
c2 = df["sales"] >= 1
result2 = df[c2]

conditions_args = [sys.argv[4], sys.argv[5]]
#conditions_args = ["false", "false"]
conditions_dfs = [result1, result2]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id","name", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id","name", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]].to_dict("records"))

print(json_final_result)
