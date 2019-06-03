import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/active_flow_rules/active_flow_rules.json', 'r') as file:
     active_flow_rules_list = json.load(file)

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

offers = []
for offer in data.values():
    if offer["flow_rule"] in active_flow_rules_list:
        offers.append(offer)

df = pd.DataFrame(offers)
df["cost"] = round(df["cost"], 2)
df["revenue"] = round(df["revenue"], 2)
df["rec_weight"] = round(df["rec_weight"], 0)
df["profit"] = round(df["profit"], 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
        2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)
df["roi"] = round(df["roi"] * 100, 2)

c1 = df["classification"] == sys.argv[2]
result1 = df[c1]

c2 = df["cost"] >= float(sys.argv[3])
result2 = df[c2]

c3 = df["profit"] <= -1 * float(sys.argv[4])
result3 = df[c3]

c4 = df["lead_cvr"] <= float(sys.argv[5])
result4 = df[c4]

c5 = df["has_mismatch_vol_weight_and_rec_weight"] == True
result5 = df[c5]

conditions_args = [sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9],
        sys.argv[10]]
conditions_dfs = [result1, result2, result3, result4, result5]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["offer_id", "offer_name", "p_offer_name", "c_offer_name", "flow_rule", "flow_rule_index", "clicks", "cost", "revenue", "profit","conversions", "lead_cvr", "epc", "cpl", "epl", "cpc", "eps", "cps", "rec_weight", "vol_weight", "classification", "has_mismatch_vol_weight_and_rec_weight","roi_score", "cvr_score", "gpr", "total_score", "roi", "sales", "leads"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("flow_rule_index", ascending=True)
json_final_result = json.dumps(final_result[["offer_id","offer_name", "p_offer_name", "c_offer_name", "flow_rule", "flow_rule_index", "clicks", "cost", "revenue", "profit","conversions", "lead_cvr", "epc", "cpl", "epl", "cpc", "eps", "cps", "rec_weight", "vol_weight", "classification", "has_mismatch_vol_weight_and_rec_weight", "roi_score", "cvr_score", "gpr", "total_score", "roi", "sales", "leads"]].to_dict("records"))

print(json_final_result)

