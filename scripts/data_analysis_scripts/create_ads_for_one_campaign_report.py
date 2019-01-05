import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
vol_id = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads_for_one_campaign/{vol_id}_{date_range}_ads_for_one_campaign_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

df = pd.DataFrame(data)
df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpa"] = round(df["cost"] / df["conversions"], 2)

# ad cost is more than xxx
c1 = df["cost"] > float(sys.argv[3])
result1 = df[c1]

# ad lost more than xxx
c2 = df["profit"] < -1 * float(sys.argv[4])
result2 = df[c2]

# ad cvr is less than or equal to xxx
c3 = np.isfinite(df["cvr"]) & (df["cvr"] <= float(sys.argv[5]))
result3 = df[c3]

conditions_args = [sys.argv[6], sys.argv[7], sys.argv[8]]
conditions_dfs = [result1, result2, result3]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["cost"]
final_result = final_result.sort_values("sort", ascending=False)
json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)

