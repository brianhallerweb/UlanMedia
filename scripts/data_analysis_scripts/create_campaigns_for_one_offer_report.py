import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
offer_id = sys.argv[2]

with open(f'/home/bsh/Documents/UlanMedia/data/campaigns_for_one_offer/{offer_id}_{date_range}_campaigns_for_one_offer_dataset.json', 'r') as file:
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

# c1 = df["cost"] > float(sys.argv[2])
# result1 = df[c1]

# c2 = df["profit"] < -1 * float(sys.argv[3])
# result2 = df[c2]

# c3 = df["cvr"] <= float(sys.argv[4])
# result3 = df[c3]

# conditions_args = [sys.argv[5], sys.argv[6], sys.argv[7]]
# conditions_dfs = [result1, result2, result3]

final_result = None 
# for i in range(len(conditions_args)):
    # if conditions_args[i] == "true" and final_result is None:
        # final_result = conditions_dfs[i]
    # elif conditions_args[i] == "true":
        # final_result = final_result.merge(conditions_dfs[i], how="inner",
        # on=["campaignID","campaignName", "clicks",
    # "cost", "revenue", "profit","conversions", "cvr",
    # "epc", "cpa"]
            # )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values(["offerFlow", "clicks"],
        ascending=[True, False])
json_final_result = json.dumps(final_result[["campaignID","campaignName", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)
