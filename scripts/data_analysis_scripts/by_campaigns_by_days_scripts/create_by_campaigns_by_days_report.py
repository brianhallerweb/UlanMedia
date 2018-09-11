import sys
import json
import pandas as pd
import numpy as np

with open(f'/home/bsh/Documents/UlanMedia/data/by_campaigns_by_days_data/by_campaigns_by_days_data.json', 'r') as file:
     data = json.load(file)

campaign_name = sys.argv[1]

df = pd.DataFrame(data[campaign_name])
df["clicks"] = df["visits"]
df["cpc"] = round(df["cost"]/df["clicks"], 3)
df["conversion_cpa"] = round(df["cost"]/df["conversions"], 2)

df = df.replace([np.inf, -np.inf], "NaN")
df = df.sort_values("day", ascending=False)

json_final_result = json.dumps(df[["name", "day", "clicks", "cost",
    "cpc", "revenue", "conversions", "conversion_cpa"]].to_dict("records"))

print(json_final_result)

