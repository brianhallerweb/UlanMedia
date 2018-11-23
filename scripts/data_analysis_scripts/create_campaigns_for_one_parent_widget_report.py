import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
#date_range = "seven"
widget_id = sys.argv[2]
#widget_id = "5718588"

with open(f'/home/bsh/Documents/UlanMedia/data/campaigns_for_one_parent_widget/{widget_id}_{date_range}_campaigns_for_one_parent_widget_dataset.json', 'r') as file:
     campaigns = json.load(file)

# 10/12 I think this is working properly. A major distinction between looking
# and child widgets and parent widgets is that a campaign will have multiple 
# parent widgets in one campaign but only 1 child widget, I think
# When I originally made the scripts to create a data set for parent widgets it 
# was overwritting parent widgets everytime a new one was encountered. I fixed
# that problem by creating a list of dictionaries, rather than a dictionary of
# dictionaries, with each vol_id as a key, as I did with the child widgets 
# data acquisition script
for campaign in campaigns:
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

# status == included
c3 = df["status"] == "included"
result3 = df[c3]

conditions_args = [sys.argv[4], sys.argv[5], sys.argv[6]]
#conditions_args = ["false", "false", "false"]
conditions_dfs = [result1, result2, result3]

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
final_result = final_result.sort_values("name", ascending=True)

# add a summary row at the bottom
summary = final_result.sum(numeric_only=True)
summary = summary.round(2)
summary["name"] = "summary"
summary["lead_cpa"] = summary["lead_cpa"] / len(final_result.index)
summary["sale_cpa"] = summary["sale_cpa"] / len(final_result.index)
final_result = final_result.append(summary, ignore_index=True)
final_result = final_result.replace(np.nan, "")


json_final_result = json.dumps(final_result[["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id","name", "lead_cpa", "sale_cpa", "profit",
            "status", "global_status"]].to_dict("records"))

print(json_final_result)
