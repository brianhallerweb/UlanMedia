import sys
import json
import pandas as pd
import numpy as np
import math

date_range = sys.argv[1]

with open(f'/home/bsh/Documents/UlanMedia/data/p_widgets_for_all_campaigns/{date_range}_p_widgets_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)
data = json_file["data"]     

# The json data is a dictionary with each widget id as a key and each widget
# (summary of all campaigns) as 
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
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)

# cost greater than x 
df = df[df["cost"] > float(sys.argv[2])]

# global status conditions 
c1 = df["global_status"] == "not yet listed"
result1 = df[c1]
c2 = df["global_status"] == "whitelist"
result2 = df[c2]
c3 = df["global_status"] == "greylist"
result3 = df[c3]
c4 = df["global_status"] == "blacklist"
result4 = df[c4]

# leads is 0
c5 = df["leads"] == 0
result5 = df[c5]

# Widget leadCVR is less than 0.25%
c6 = df["lead_cvr"] < .25
result6 = df[c6]

# Widget saleCPA is more than $500
c7 = np.isfinite(df["sale_cpa"]) & (df["sale_cpa"] > 500)
result7 = df[c7]

# Widget lost more than $100
c8 = df["profit"] < -100
result8 = df[c8]

conditions_args = [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6],
        sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]
conditions_dfs = [result1, result2, result3, result4, result5, result6, result7, result8]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id", "lead_cpa", "lead_cvr", "sale_cpa", "profit",
            "status", "global_status", "has_children"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", "referrer",
            "revenue", "sales", "widget_id", "lead_cpa","lead_cvr", "sale_cpa", "profit",
            "status", "global_status", "has_children"]].to_dict("records"))

print(json_final_result)