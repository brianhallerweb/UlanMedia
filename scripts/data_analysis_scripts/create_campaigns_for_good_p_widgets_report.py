import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
# date_range = "oneeighty"

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json', 'r') as file:
     campaigns = json.load(file)

df = pd.DataFrame(campaigns)

df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cost"] = round(df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)

final_result = df
final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("name", ascending=True)

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
            "cpc", "epc", "mpc", "cpl", "epl", "mpl", "lead_cvr",
            "cps", "eps", "mps", "profit", "status",
            "widget_id", "global_status", "campaign_bid",
            "widget_bid", "bid_coefficient", "recommended_widget_bid",
            "recommended_coefficient"]].to_dict("records"))

print(json_final_result)
