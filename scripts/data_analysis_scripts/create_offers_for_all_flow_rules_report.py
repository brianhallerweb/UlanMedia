import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_all_flow_rules/{date_range}_offers_for_all_flow_rules_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

offers = []
for offer in data.values():
    offers.append(offer)

df = pd.DataFrame(offers)
df["cost"] = round(df["cost"], 2)
df["revenue"] = round(df["revenue"], 2)
df["profit"] = round(df["profit"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpa"] = round(df["cost"] / df["conversions"], 2)
df["cpc"] = round(df["clicks"] / df["cost"], 2)
df["epa"] = round(df["revenue"] / df["conversions"], 2)


c1 = df["cost"] > float(sys.argv[2])
result1 = df[c1]

c2 = df["profit"] < -1 * float(sys.argv[3])
result2 = df[c2]

c3 = df["cvr"] <= float(sys.argv[4])
result3 = df[c3]

conditions_args = [sys.argv[5], sys.argv[6], sys.argv[7]]
conditions_dfs = [result1, result2, result3]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["offer_id","offer_name", "p_offer_name", "c_offer_name", "flow_rule", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa", "cpc", "epa"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
# final_result = final_result.sort_values(["flow_rule", "clicks"],
        # ascending=[True, False])
final_result = final_result.sort_values("flow_rule", ascending=True)
json_final_result = json.dumps(final_result[["offer_id","offer_name", "p_offer_name", "c_offer_name",
    "flow_rule", "clicks", "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa", "cpc", "epa"]].to_dict("records"))

print(json_final_result)

