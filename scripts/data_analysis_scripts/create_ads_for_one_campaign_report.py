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
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epa"] = round(df["revenue"] / df["conversions"], 2)
df["roi"] = round(df["roi"] * 100, 2)
df["ctr"] = round(df["ctr"] * 100, 2)
df["ppi"] = round(df["profit"] / df["imps"], 6)
df["local_rank"] = round(df["local_rank"], 0)
df["final_rank"] = round(df["final_rank"], 0)
df["global_rank"] = round(df["global_rank"], 0)

c1 = df["classification"] == sys.argv[3]
result1 = df[c1]

c2 = df["cost"] > float(sys.argv[4])
result2 = df[c2]

c3 = df["profit"] < -1 * float(sys.argv[5])
result3 = df[c3]

c4 = df["ctr"] <= float(sys.argv[6])
result4 = df[c4]

c5 = np.isfinite(df["cvr"]) & (df["cvr"] <= float(sys.argv[7]))
result5 = df[c5]

conditions_args = [sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11],
        sys.argv[12]]
conditions_dfs = [result1, result2, result3, result4, result5]


final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa", "cpc","epa", "roi", "classification", "local_rank",
    "local_rank_order", "final_rank", "final_rank_order",
    "global_rank", "global_rank_order", "imps", "ctr", "ppi" ] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["final_rank"]
final_result = final_result.sort_values("sort", ascending=False)

# add a summary row at the top
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["image"] = "summary"
    summary["local_rank"] = "NA"
    summary["local_rank_order"] = "NA"
    summary["final_rank"] = "NA"
    summary["final_rank_order"] = "NA"
    summary["global_rank"] = "NA"
    summary["global_rank_order"] = "NA"
    summary["classification"] = "NA"
    summary["roi"] = round(summary["profit"] / summary["cost"], 2)
    summary["ctr"] = round((summary["clicks"] / summary["imps"]) * 100,
        2)
    summary["ppi"] = round((summary["profit"] / summary["imps"]),
        6)
    if summary["clicks"] == 0:
        summary["cvr"] = 0
        summary["epc"] = 0
    else:
        summary["cvr"] = round((summary["conversions"] / summary["clicks"]) * 100,
        2)
        summary["epc"] = round((summary["revenue"] / summary["clicks"]),
        2)
    if summary["conversions"] == 0:
        summary["cpa"] = 0
        summary["epa"] = 0
    else:
        summary["cpa"] = round((summary["cost"] / summary["conversions"]),
        2)
        summary["epa"] = round((summary["revenue"] / summary["conversions"]),
        2)
    final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
    final_result = final_result.replace(np.nan, "")


json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa", "cpc","epa", "roi", "classification",
    "local_rank", "local_rank_order", "final_rank", "final_rank_order",
    "global_rank", "global_rank_order", "imps", "ctr", "ppi"]].to_dict("records"))

print(json_final_result)

