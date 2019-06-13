import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
domain = sys.argv[2]
# date_range = "oneeighty" 
# domain = "ru-clip.net"


with open(f'{os.environ.get("ULANMEDIAAPP")}/data/widgets_for_one_domain_for_all_campaigns/{date_range}_{domain}_widgets_for_one_domain_for_all_campaigns_dataset.json', 'r') as file:
     json_file = json.load(file)

metadata = json_file["metadata"]
data = json_file["data"]

widgets = []
for widget in data.values():
    widgets.append(widget)

df = pd.DataFrame(widgets)

df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)
# df["w_bid"] = round(df["w_bid"], 2)
# df["rec_w_bid"] = round(df["rec_w_bid"], 2)
# df["rec_coeff"] = round(df["rec_coeff"], 1)

# c1 = df["classification"] == sys.argv[3]
# result1 = df[c1]

# c2 = df["status"] == sys.argv[4]
# result2 = df[c2]

# c3 = df["global_status"] == sys.argv[5]
# result3 = df[c3]

# c4 = df["cost"] >= float(sys.argv[6])
# result4 = df[c4]

# c5 = df["profit"] <= -1 * float(sys.argv[7])
# result5 = df[c5]

# c6 = df["is_bad_and_included"] == True 
# result6 = df[c6]

# conditions_args = [sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13]]
# conditions_dfs = [result1, result2, result3, result4, result5, result6]

# final_result = None 
# for i in range(len(conditions_args)):
    # if conditions_args[i] == "true" and final_result is None:
        # final_result = conditions_dfs[i]
    # elif conditions_args[i] == "true":
        # final_result = final_result.merge(conditions_dfs[i], how="inner",
        # on=["clicks", "cost", "leads", "revenue", "sales","vol_id", "mgid_id", "widget_id", "cpc",
    # "epc", "cpl", "epl", "mpl", "cps", "eps", "mps" ,"lead_cvr",
    # "profit", "status", "global_status", "classification",
    # "is_bad_and_included", "w_bid", "coeff", "rec_w_bid",
            # "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
            # "mismatch_coeff_and_rec_coeff", "domain"]
            # )

# if final_result is None:
    # final_result = df
final_result = df

final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

json_final_result = json.dumps(final_result[["clicks", "cost", "leads",
    "revenue", "sales","widget_id", "cpc",
    "epc", "cpl", "epl", "cps", "eps", "lead_cvr",
    "profit", "global_status", "classification", "domain"]].to_dict("records"))

print(json_final_result)
