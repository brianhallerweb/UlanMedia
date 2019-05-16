import sys
import os
import json
import pandas as pd
import numpy as np

c_widget_id = sys.argv[1]
campaign_id = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/months_for_one_c_widget_for_one_campaign/{c_widget_id}_{campaign_id}_months_for_one_c_widget_for_one_campaign_dataset.json', 'r') as file:
    data = json.load(file)

months = []
for month in data["data"]:
    months.append(data["data"][month])
    
df = pd.DataFrame(months)

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
df = df.sort_values("month_index", ascending=True)

json_final_result = json.dumps(df[["clicks", "cost", "month", "month_index", "revenue",
    "profit", "leads", "sales",
    "lead_cvr", "epc", "cpl", "cps", "cpc", "epl", "eps", "roi"]].to_dict("records"))

print(json_final_result)
