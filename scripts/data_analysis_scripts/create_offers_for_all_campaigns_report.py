import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]

with open(f'/home/bsh/Documents/UlanMedia/data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)

data = json_file["data"]

offers = []
for offer in data.values():
    offers.append(offer)

df = pd.DataFrame(offers)
df["cost"] = round(df["cost"], 2)
df["revenue"] = round(df["profit"] + df["cost"], 2)
df["profit"] = round(df["profit"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpa"] = round(df["cost"] / df["conversions"], 2)

final_result = df.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["offerFlow"]
final_result = final_result.sort_values("sort", ascending=False)
json_final_result = json.dumps(final_result[["offerID","offerName", "offerFlow", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)

