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


c1 = (df["profit"] < -20) 
result1 = df[c1]

conditions_args = [sys.argv[2]]
conditions_dfs = [result1]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        # This outer joint will need changing when and if I add more conditions
        # it is currently not running because there is only one condition.
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["image"] )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["image"]
final_result = final_result.sort_values("sort")
json_final_result = json.dumps(final_result[["image", "clicks",
    "cost", "revenue", "profit","conversions", "cvr",
    "epc", "cpa", "status"]].to_dict("records"))

print(json_final_result)

