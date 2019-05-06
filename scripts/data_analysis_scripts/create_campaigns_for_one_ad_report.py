import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
ad_image = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_one_ad/{ad_image}_{date_range}_campaigns_for_one_ad_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

df = pd.DataFrame(data)
df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
        2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)
df["roi"] = round(df["roi"] * 100, 2)
df["ctr"] = round(df["ctr"] * 100, 2)
df["ppi"] = round(df["profit"] / df["imps"], 6) 

c1 = df["cost"] >= float(sys.argv[3])
result1 = df[c1]

c2 = df["profit"] <= -1 * float(sys.argv[4])
result2 = df[c2]

c3 = df["ctr"] <= float(sys.argv[5])
result3 = df[c3]

c4 = np.isfinite(df["lead_cvr"]) & (df["lead_cvr"] <= float(sys.argv[6]))
result4 = df[c4]

conditions_args = [sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]]
conditions_dfs = [result1, result2, result3, result4]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["image", "clicks",
    "cost", "revenue", "profit","conversions", "lead_cvr",
    "cpc", "epc", "cpl", "epl", "cps", "eps", "roi", "name", "mgid_id", "vol_id", "ctr",
    "imps", "ppi", "leads", "sales"] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["cost"]
final_result = final_result.sort_values("sort", ascending=False)

# add a summary row at the top
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["name"] = "summary"
    summary["roi"] = round(summary["profit"] / summary["cost"], 2)
    summary["ctr"] = round((summary["clicks"] / summary["imps"]) * 100,
        2)
    summary["ppi"] = round((summary["profit"] / summary["imps"]),
        6)
    if summary["clicks"] == 0:
        summary["lead_cvr"] = 0
        summary["epc"] = 0
    else:
        summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
        2)
        summary["epc"] = round((summary["revenue"] / summary["clicks"]),
        2)
    if summary["leads"] == 0:
        summary["cpl"] = 0
        summary["epl"] = 0
    else:
        summary["cpl"] = round((summary["cost"] / summary["leads"]),
        2)
        summary["epl"] = round((summary["revenue"] / summary["leads"]),
        2)
    if summary["sales"] == 0:
        summary["cps"] = 0
        summary["eps"] = 0
    else:
        summary["cps"] = round((summary["cost"] / summary["sales"]),
        2)
        summary["eps"] = round((summary["revenue"] / summary["sales"]),
        2)
    final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
    final_result = final_result.replace(np.nan, "")

json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "lead_cvr",
    "cpc", "epc", "cpl", "epl", "cps", "eps", "roi", "name", "mgid_id", "vol_id", "ctr",
    "imps", "ppi", "leads", "sales"]].to_dict("records"))

print(json_final_result)

