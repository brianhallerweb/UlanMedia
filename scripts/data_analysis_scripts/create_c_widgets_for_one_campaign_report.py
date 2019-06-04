import sys
import os
import json
import pandas as pd
import numpy as np

date_range = sys.argv[1]
volid = sys.argv[2]

with open(f'{os.environ.get("ULANMEDIAAPP")}/data/c_widgets_for_one_campaign/{volid}_{date_range}_c_widgets_for_one_campaign_dataset.json', 'r') as file:
     json_file = json.load(file)

metadata = json_file["metadata"]
data = json_file["data"]

df = pd.DataFrame(data)

df["cost"] = round(df["cost"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
df["lead_cvr"] = round(df["leads"] / df["clicks"] * 100, 2)
df["cpc"] = round(df["cost"] / df["clicks"], 2)
df["epc"] = round(df["revenue"] / df["clicks"], 2)
df["cpl"] = round(df["cost"] / df["leads"], 2)
df["epl"] = round(df["revenue"] / df["leads"], 2)
df["cps"] = round(df["cost"] / df["sales"], 2)
df["eps"] = round(df["revenue"] / df["sales"], 2)
df["w_bid"] = round(df["w_bid"], 2)
df["rec_w_bid"] = round(df["rec_w_bid"], 2)
df["rec_coeff"] = round(df["rec_coeff"], 1)

c1 = df["classification"] == sys.argv[3]
result1 = df[c1]

c2 = df["status"] == sys.argv[4]
result2 = df[c2]

c3 = df["global_status"] == sys.argv[5]
result3 = df[c3]

c4 = df["cost"] >= float(sys.argv[6])
result4 = df[c4]

c5 = df["profit"] <= -1 * float(sys.argv[7])
result5 = df[c5]

c6 = df["is_bad_and_included"] == True 
result6 = df[c6]

conditions_args = [sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13]]
conditions_dfs = [result1, result2, result3, result4, result5, result6]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="inner",
        on=["clicks", "cost", "leads", "revenue", "sales","vol_id", "mgid_id", "widget_id", "cpc",
    "epc", "cpl", "epl", "mpl", "cps", "eps", "mps" ,"lead_cvr",
    "profit", "status", "global_status", "classification",
    "is_bad_and_included", "w_bid", "coeff", "rec_w_bid",
            "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
            "mismatch_coeff_and_rec_coeff"]
            )

if final_result is None:
    final_result = df

final_result = final_result.replace([np.inf, -np.inf], "NaN")
final_result = final_result.replace(np.nan, "NaN")
final_result = final_result.sort_values("cost", ascending=False)

# add a summary row at the top
if len(final_result.index) > 0:
    summary = final_result.sum(numeric_only=True)
    summary = summary.round(2)
    summary["widget_id"] = "summary"
    summary["cpc"] = round(summary["cost"] / summary["clicks"], 2)
    summary["epc"] = round(summary["revenue"] / summary["clicks"], 2)
    number_of_rows = len(final_result.index)
    summary["mpl"] = round(summary["mpl"] / number_of_rows, 2)
    summary["mps"] = round(summary["mps"] / number_of_rows, 2)
    summary["classification"] = "NA"
    summary["w_bid"] = "NA"
    summary["coeff"] = "NA"
    summary["rec_w_bid"] = "NA"
    summary["rec_coeff"] = "NA"
    summary["status"] = "NA"
    summary["global_status"] = "NA"
    summary["is_bad_and_included"] = False 
    if summary["clicks"] == 0:
        summary["lead_cvr"] = 0
    else:
        summary["lead_cvr"] = round((summary["leads"] / summary["clicks"]) * 100,
        2)
    rows_with_leads = final_result[final_result["leads"] >= 1]
    number_of_rows_with_leads = len(rows_with_leads.index)
    if number_of_rows_with_leads > 0:
        summary["cpl"] = round(summary["cost"] / summary["leads"], 2)
        summary["epl"] = round(summary["revenue"] / summary["leads"], 2)
    else:
        summary["cpl"] = 0 
        summary["epl"] = 0
    rows_with_sales = final_result[final_result["sales"] >= 1]
    number_of_rows_with_sales = len(rows_with_sales.index)
    if number_of_rows_with_sales > 0:
        summary["cps"] = round(summary["cost"] / summary["sales"], 2)
        summary["eps"] = round(summary["revenue"] / summary["sales"], 2)
    else:
        summary["cps"] = 0
        summary["eps"] = 0
    # Append summary onto the top
    final_result = pd.concat([pd.DataFrame(summary).transpose(),final_result])
    final_result = final_result.replace(np.nan, "")


json_final_result = json.dumps(final_result[["clicks", "cost", "leads",
    "revenue", "sales","vol_id", "mgid_id", "widget_id", "cpc",
    "epc", "cpl", "epl", "mpl", "cps", "eps", "mps" ,"lead_cvr",
    "profit", "status", "global_status", "classification",
    "is_bad_and_included", "w_bid", "coeff", "rec_w_bid",
            "rec_coeff", "mismatch_w_bid_and_rec_w_bid",
            "mismatch_coeff_and_rec_coeff"]].to_dict("records"))

print(json_final_result)
