import sys
import os
import json
import pandas as pd
import numpy as np
import math

date_range = sys.argv[1]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/c_widgets_for_all_campaigns/{date_range}_c_widgets_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)
data = json_file["data"]     

# The json data is a dictionary with each widget id as a key and each widget
# (summary of all campaigns) as 
# a value. The loop below simple takes the values and puts them into a list. 
widgets = []
for widget in data.values():
    widgets.append(widget)

df = pd.DataFrame(widgets)

df["cost"] = round(df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)

c1 = df["classification"] == sys.argv[2]
result1 = df[c1]

c2 = df["global_status"] == sys.argv[3]
result2 = df[c2]

c3 = df["cost"] > float(sys.argv[4])
result3 = df[c3]

c4 = df["profit"] < -1 * float(sys.argv[5])
result4 = df[c4]

mismatch1 = (df["classification"] == "white") & ((df["global_status"] ==
        "c_greylist") | (df["global_status"] ==
        "pc_greylist") | (df["global_status"] ==
        "c_blacklist") | (df["global_status"] ==
        "pc_blacklist"))

mismatch2 = (df["classification"] == "grey") & ((df["global_status"] ==
        "c_whitelist") | (df["global_status"] ==
        "pc_whitelist") | (df["global_status"] ==
        "c_blacklist") | (df["global_status"] ==
        "pc_blacklist"))

mismatch3 = (df["classification"] == "black") & ((df["global_status"] ==
        "c_whitelist") | (df["global_status"] ==
        "pc_whitelist") | (df["global_status"] ==
        "c_greylist") | (df["global_status"] ==
        "pc_greylist"))

c5 = mismatch1 | mismatch2 | mismatch3
result5 = df[c5]

c6 = df["has_included_bad_campaigns"] == True 
result6 = df[c6]

conditions_args = [sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11]]
conditions_dfs = [result1, result2, result3, result4, result5, result6]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id", "lead_cvr", "profit",
            "global_status", "classification", "has_included_bad_campaigns",
            "good_campaigns_count", "bad_campaigns_count",
            "wait_campaigns_count", "cpc", "epc", "cpl", "epl", "cps", "eps"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values(["profit", "classification"],
        ascending=[True, True])


json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id", "lead_cvr", "profit",
            "global_status", "classification", "has_included_bad_campaigns",
            "good_campaigns_count", "bad_campaigns_count",
            "wait_campaigns_count", "cpc", "epc", "cpl", "epl", "cps", "eps"]].to_dict("records"))

print(json_final_result)
