import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
vol_id = sys.argv[2]
# date_range = "seven"
# vol_id = "4ff2a836-8790-4e07-9f45-98b05c3a393a"

with open(f'/home/bsh/Documents/UlanMedia/data/ads_for_one_campaign/{vol_id}_{date_range}_ads_for_one_campaign_dataset.json', 'r') as file:
     data = json.load(file)

df = pd.DataFrame(data)
df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
# epc uses the series.round method. It doesn't appear to do anything different
# from python's round()
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpa"] = round(df["cost"] / df["conversions"], 2)

# The prerequisite condition for every report
final_result = df[df["epc"] >= float(sys.argv[3])]
# final_result = df[df["epc"] >= 0]

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["cost"]
final_result = final_result.sort_values("sort", ascending=False)
json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)

