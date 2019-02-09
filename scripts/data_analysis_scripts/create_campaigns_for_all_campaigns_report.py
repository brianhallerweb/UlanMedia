import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_all_campaigns/{date_range}_campaigns_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)

metadata = json_file["metadata"]
data = json_file["data"]

df = pd.DataFrame(data)
df["vol_start_date"] = metadata["vol_start_date"]
df["vol_end_date"] = metadata["vol_end_date"]
df["mgid_start_date"] = metadata["mgid_start_date"]
df["mgid_end_date"] = metadata["mgid_end_date"]
df["mpl"] = df["max_lead_cpa"].astype("float64")
df["mps"] = df["max_sale_cpa"].astype("float64")
df["mpc"] = df["max_cpc"].astype("float64")
df["cpc"] = round(df["cost"] / df["clicks"], 3)
df["epc"] = round(df["revenue"] / df["clicks"], 3)
df["cpl"] = round(df["cost"] / df["leads"], 3)
df["epl"] = round(df["revenue"] / df["leads"], 3)
df["eps"] = round(df["revenue"] / df["sales"], 3)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)

c1 = df["cpc"] > df["epc"]
result1 = df[c1]

c2 = df["cpc"] > df["epc"]
result2 = df[c2]

c3 = df["cpc"] > df["epc"]
result3 = df[c3]

conditions_args = [sys.argv[2], sys.argv[3], sys.argv[4]]
conditions_dfs = [result1, result2, result3]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["mgid_start_date", "mgid_end_date","vol_start_date", "vol_end_date","mgid_id", "vol_id", "name", "clicks",
            "cost", "imps", "leads", "mpl", "mps", "cpc",
            "epc", "epl",
            "mgid_id", "revenue", "sales","vol_id", "cpl", "eps", "cps", "mpc",
            "profit"] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["name"].str[4:]
final_result = final_result.sort_values("sort")
json_final_result = json.dumps(final_result[["mgid_start_date",
    "mgid_end_date","vol_start_date", "vol_end_date", "vol_id", "name",
    "clicks", "cost", "revenue", "profit", "leads","mpc",
    "mpl","cpl", "epl", "sales", "cps","mps","cpc","eps", "epc"]].to_dict("records"))

print(json_final_result)

