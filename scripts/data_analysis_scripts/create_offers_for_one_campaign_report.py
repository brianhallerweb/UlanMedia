import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
campaign_id = sys.argv[2]

with open(f'/home/bsh/Documents/UlanMedia/data/offers_for_one_campaign/{campaign_id}_{date_range}_offers_for_one_campaign_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

df = pd.DataFrame(data)
df["cost"] = round(df["cost"], 2)
df["revenue"] = round(df["profit"] + df["cost"], 2)
df["profit"] = round(df["profit"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpa"] = round(df["cost"] / df["conversions"], 2)

c1 = df["cost"] > float(sys.argv[3])
result1 = df[c1]

c2 = df["profit"] < -1 * float(sys.argv[4])
result2 = df[c2]

c3 = df["cvr"] <= float(sys.argv[5])
result3 = df[c3]

conditions_args = [sys.argv[6], sys.argv[7], sys.argv[8]]
conditions_dfs = [result1, result2, result3]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["offerID","offerName", "offerFlow", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values(["offerFlow", "clicks"],
        ascending=[True, False])

if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["offerFlow"] = "summary"
    if summary["clicks"] == 0:
        summary["cvr"] = 0
        summary["epc"] = 0
    else:
        summary["cvr"] = round((summary["conversions"] / summary["clicks"]) * 100,
        2)
        summary["epc"] = round(summary["revenue"] / summary["clicks"], 3)
    if summary["conversions"] == 0:
        summary["cpa"] = 0
    else:
        summary["cpa"] = round(summary["cost"] / summary["conversions"], 2)
    final_result = final_result.append(summary, ignore_index=True)
    final_result = final_result.replace(np.nan, "")

json_final_result = json.dumps(final_result[["offerID","offerName", "offerFlow", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)

