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

c1 = df["classification"] == sys.argv[2]
result1 = df[c1]

c2 = df["cost"] > float(sys.argv[3])
result2 = df[c2]

c3 = df["profit"] < -1 * float(sys.argv[4])
result3 = df[c3]

c4 = df["sales"] > float(sys.argv[5])
result4 = df[c4]

c5 = df["cpc"] > df["epc"]
result5 = df[c5]

c6 = df["cpc"] > df["epc"]
result6 = df[c6]

c7 = df["cpc"] > df["epc"]
result7 = df[c7]

c8 = df["epc"] > df["cpc"]
result8 = df[c8]

c9 = df["epl"] > df["cpl"]
result9 = df[c9]

c10 = df["eps"] > df["cps"]
result10 = df[c10]

c11 = df["mpc"] >= (df["epc"] + (df["epc"]*float(sys.argv[6])/100))
result11 = df[c11]

c12 = df["mpl"] >= (df["epl"] + (df["epl"]*float(sys.argv[7])/100))
result12 = df[c12]

c13 = df["mps"] >= (df["eps"] + (df["eps"]*float(sys.argv[8])/100))
result13 = df[c13]

c14 = df["mpc"] >= (df["epc"] - (df["epc"]*float(sys.argv[9])/100))
result14 = df[c14]

c15 = df["mpl"] >= (df["epl"] - (df["epl"]*float(sys.argv[10])/100))
result15 = df[c15]

c16 = df["mps"] >= (df["eps"] - (df["eps"]*float(sys.argv[11])/100))
result16 = df[c16]

c17 = df["cpc"] >= (df["mpc"] + (df["mpc"]*float(sys.argv[12])/100))
result17 = df[c17]

c18 = df["cpl"] >= (df["mpl"] + (df["mpl"]*float(sys.argv[13])/100))
result18 = df[c18]

c19 = df["cps"] >= (df["mps"] + (df["mps"]*float(sys.argv[14])/100))
result19 = df[c19]

c20 = df["cpc"] >= (df["mpc"] - (df["mpc"]*float(sys.argv[15])/100))
result20 = df[c20]

c21 = df["cpl"] >= (df["mpl"] - (df["mpl"]*float(sys.argv[16])/100))
result21 = df[c21]

c22 = df["cps"] >= (df["mps"] - (df["mps"]*float(sys.argv[17])/100))
result22 = df[c22]

conditions_args = [sys.argv[18],
        sys.argv[19], sys.argv[20], sys.argv[21], sys.argv[22],
        sys.argv[23], sys.argv[24], sys.argv[25], sys.argv[26], sys.argv[27],
        sys.argv[28], sys.argv[29], sys.argv[30],
        sys.argv[31], sys.argv[32], sys.argv[33], sys.argv[34], sys.argv[35],
        sys.argv[36], sys.argv[37], sys.argv[38], sys.argv[39]]
conditions_dfs = [result1, result2, result3, result4, result5, result6,
        result7, result8, result9, result10, result11, result12, result13,
        result14, result15, result16, result17, result18, result19, result20, result21, result22]

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
            "profit", "classification"] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["name"].str[4:]
final_result = final_result.sort_values("sort")
json_final_result = json.dumps(final_result[["mgid_start_date",
    "mgid_end_date","vol_start_date", "vol_end_date", "mgid_id", "vol_id", "name",
    "clicks", "cost", "revenue", "profit", "leads","mpc",
    "mpl","cpl", "epl", "sales", "cps","mps","cpc","eps", "epc", "classification"]].to_dict("records"))

print(json_final_result)

