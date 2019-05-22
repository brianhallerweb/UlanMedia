import sys
import os
import json
import pandas as pd
import numpy as np

ad_image = sys.argv[1]
# ad_image = "cashpile3.jpg"

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/days_for_one_ad_for_all_campaigns/{ad_image}_days_for_one_ad_for_all_campaigns_dataset.json', 'r') as file:
    data = json.load(file)

days = []
for day in data["data"]:
    days.append(data["data"][day])
    
df = pd.DataFrame(days)

df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["profit"], 2)
df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
        2)
df["epc"] = (df["revenue"] / df["clicks"]).round(3)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)
df["roi"] = round((df["profit"] / df["cost"])*100, 2)


df = df.replace([np.inf, -np.inf], "NaN")
df = df.replace(np.nan, "NaN")
df = df.sort_values("day", ascending=False)

json_final_result = json.dumps(df[["clicks", "cost", "day", "revenue",
    "profit", "leads", "sales",
    "lead_cvr", "epc", "cpl", "cps", "cpc", "epl", "eps", "roi"]].to_dict("records"))

print(json_final_result)

