import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
widget_id = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/campaigns_for_one_p_widget/{widget_id}_{date_range}_campaigns_for_one_p_widget_dataset.json', 'r') as file:
     json_file = json.load(file)

campaigns = json_file["data"]

df = pd.DataFrame(campaigns)

# this condition handles the case where the parent widget dataset is empty.
# The first time I noticed this possibility was when mike excluded a widget
# from all campaigns. The next day, when the app created a dataset for
# campaigns_for_one_parent/child_widget, that dataset was empty. 
if len(df.index) == 0:
    print(json.dumps(campaigns))
    sys.exit()

df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["cost"] = round(df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)

# status conditions (all, included, excluded)
c1 = df["status"] == sys.argv[3]
result1 = df[c1]

# global status conditions (not yet listed, whitelist, greylist, blacklist)
c2 = df["global_status"] == sys.argv[4]
result2 = df[c2]

# widget cost is more than xxx
c3 = df["cost"] > float(sys.argv[5])
result3 = df[c3]

# widget lost more than xxx
c4 = df["profit"] < -1 * float(sys.argv[6])
result4 = df[c4]

# widget leadCVR is less than or equal to xxx
c5 = np.isfinite(df["lead_cvr"]) & (df["lead_cvr"] <= float(sys.argv[7]))
result5 = df[c5]

# widget clicks are >= xxx OR cost >= xxx
c6 = (df["clicks"] >= float(sys.argv[8])) | (df["cost"] >= float(sys.argv[9]))
result6= df[c6]

conditions_args = [sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13],
        sys.argv[14], sys.argv[15]]
conditions_dfs = [result1, result2, result3, result4, result5, result6]


final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
            "max_lead_cpa", "lead_cpa", "lead_cvr",
            "max_sale_cpa", "sale_cpa", "profit", "status", "global_status"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("name", ascending=True)

# add a summary row at the bottom
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["name"] = "summary"
    if summary["clicks"] == 0:
        summary["lead_cvr"] = 0
    else:
        summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
        2)
    rows_with_leads = final_result[final_result["leads"] >= 1]
    number_of_rows_with_leads = len(rows_with_leads.index)
    if number_of_rows_with_leads > 0:
        summary["lead_cpa"] = round(summary["cost"] / summary["leads"], 2)
    else:
        summary["lead_cpa"] = 0 
    rows_with_sales = final_result[final_result["sales"] >= 1]
    number_of_rows_with_sales = len(rows_with_sales.index)
    if number_of_rows_with_sales > 0:
        summary["sale_cpa"] = round(summary["cost"] / summary["sales"], 2)
    else:
        summary["sale_cpa"] = 0
    final_result = final_result.append(summary, ignore_index=True)
    final_result = final_result.replace(np.nan, "")

json_final_result = json.dumps(final_result[["clicks", "cost", "leads", 
            "revenue", "sales", "widget_id","name", "vol_id", "mgid_id",
            "max_lead_cpa", "lead_cpa","lead_cvr", "max_sale_cpa", "sale_cpa", "profit",
            "status", "global_status"]].to_dict("records"))

print(json_final_result)
