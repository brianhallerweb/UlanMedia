import sys
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]

with open(f'/home/bsh/Documents/UlanMedia/data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json', 'r') as file:
     data = json.load(file)

# The json data is a dictionary with each ad_image name as a key and the
# summaries of each ad stats as a value
# The loop below simple takes the values and puts them into a list. 
ads = []
for ad in data.values():
    ads.append(ad)

df = pd.DataFrame(ads)
df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cvr"] = round((df["conversions"] / df["clicks"]) * 100,
        2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpa"] = round(df["cost"] / df["conversions"], 2)

# The prerequisite condition for every report
final_result = df[df["epc"] >= float(sys.argv[2])]

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["cost"]
final_result = final_result.sort_values("sort", ascending=False)
json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa"]].to_dict("records"))

print(json_final_result)

