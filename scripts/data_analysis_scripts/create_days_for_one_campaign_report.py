import sys
import os
import json
import pandas as pd
import numpy as np

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/days_for_one_campaign/days_for_one_campaign_dataset.json', 'r') as file:
     data = json.load(file)

campaign_id = sys.argv[1]

df = pd.DataFrame(data[campaign_id])

        # Day, Cost, Revenue, Profit, Clicks, CPC, EPC, Conversions, CPA, EPA
        # (revenue/convs), CVR

df["cost"] = round(df["cost"], 2)
df["revenue"] = round((df["profit"] - df["cost"]), 2)
df["cpc"] = round(df["cost"]/df["clicks"], 3)
df["cpa"] = round(df["cost"]/df["conversions"], 2)

df = df.replace([np.inf, -np.inf], 0)
df = df.replace(np.nan, "NaN")
df = df.sort_values("day", ascending=False)

json_final_result = json.dumps(df[["vol_id", "name", "day", "clicks", "cost",
    "cpc", "revenue", "conversions", "cpa"]].to_dict("records"))

print(json_final_result)

