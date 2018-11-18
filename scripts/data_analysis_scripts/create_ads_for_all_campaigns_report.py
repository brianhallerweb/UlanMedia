import sys
import json
import pandas as pd
import numpy as np

# date_range = sys.argv[1]
date_range = "yesterday"

with open(f'/home/bsh/Documents/UlanMedia/data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json', 'r') as file:
     data = json.load(file)

# The json data is a dictionary with each ad_image name as a key and the
# summaries of each ad stats as a value
# The loop below simple takes the values and puts them into a list. 
ads = []
for ad in data.values():
    ads.append(ad)

df = pd.DataFrame(ads)
df["profit"] = df["ad_revenue"] - df["ad_cost"]
df["conversion_rate"] = round((df["ad_conversions"] / df["ad_clicks"]) * 100,
        3)
df["epc"] = round(df["ad_revenue"] / df["ad_clicks"], 3)
df["cpa"] = round(df["ad_cost"] / df["ad_conversions"], 3)

# I have a decent spreadsheet developing. The data looks suspiscious so check
# its accuracy and then proceed. 
print(df[["ad_image", "profit", "conversion_rate", "epc", "cpa"]])
sys.exit()

# The prerequisite condition for every report
df = df[df["profit"] < -1 * float(sys.argv[2]) * df["max_sale_cpa"]]

# clicks > 1000 and leads = 0
c1 = (df["clicks"] > 1000) & (df["leads"] == 0)
result1 = df[c1]

#cost > 0.25*maxSaleCPA && leadCPA > 3*maxLeadCPA
c2 = (df["cost"] > 0.25*df["max_sale_cpa"]) & (df["lead_cpa"] > 3*df["max_lead_cpa"])
result2 = df[c2]
    
# cost > 0.3*maxSaleCPA and leadCPA > 2*maxLeadCPA 
c3 = (df["cost"] > 0.3*df["max_sale_cpa"]) & (df["lead_cpa"] >
2*df["max_lead_cpa"])
result3 = df[c3] 

# cost > 0.5*maxSaleCPA and leadCPA > 1.5*maxLeadCPA    
c4 = (df["cost"] > 0.5*df["max_sale_cpa"]) & (df["lead_cpa"] >
1.5*df["max_lead_cpa"])
result4 = df[c4]

# cost > 2*maxSaleCPA and leadCPA > maxLeadCPA 
c5 = (df["cost"] > 2*df["max_sale_cpa"]) & (df["lead_cpa"] > df["max_lead_cpa"])
result5 = df[c5]

conditions_args = [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6],
        sys.argv[7]]
conditions_dfs = [result1, result2, result3, result4, result5]

final_result = None 
for i in range(len(conditions_args)):
    if conditions_args[i] == "true" and final_result is None:
        final_result = conditions_dfs[i]
    elif conditions_args[i] == "true":
        final_result = final_result.merge(conditions_dfs[i], how="outer",
        on=["mgid_id", "vol_id", "name", "clicks",
            "cost", "imps", "leads", "max_lead_cpa", "max_sale_cpa", "epc",
            "mgid_id", "revenue", "sales","vol_id", "lead_cpa", "sale_cpa",
            "profit"] )

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result = final_result.replace(np.nan, "NaN")
final_result["sort"] = final_result["name"].str[4:]
final_result = final_result.sort_values("sort")
json_final_result = json.dumps(final_result[["mgid_id", "vol_id", "name", "clicks", "cost", "revenue", "profit", "leads","lead_cpa", "max_lead_cpa", "sales", "sale_cpa","max_sale_cpa","epc"]].to_dict("records"))

print(json_final_result)

