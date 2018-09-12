import sys
import json
import pandas as pd
import numpy as np

filename = sys.argv[1]

with open(f'/home/bsh/Documents/UlanMedia/data/by_campaigns_data/{filename}.json', 'r') as file:
     data = json.load(file)

df = pd.DataFrame(data)
df["max_lead_cpa"] = df["max_lead_cpa"].astype("float64")
df["max_sale_cpa"] = df["max_sale_cpa"].astype("float64")
df["epc"] = round(df["revenue"] / df["clicks"], 3)
df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
df["profit"] = round(df["revenue"] - df["cost"], 2)
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
        final_result = final_result.merge(conditions_dfs[i], how="outer", on=["name", "clicks",
            "cost", "imps", "leads", "max_lead_cpa", "max_sale_cpa", "epc",
            "mgid_id", "revenue", "sales","vol_id", "lead_cpa", "sale_cpa",
            "profit"] )

final_result = final_result.replace([np.inf, -np.inf], 0)
final_result["sort"] = final_result["name"].str[4:]
final_result = final_result.sort_values("sort")
json_final_result = json.dumps(final_result[["name", "clicks", "cost", "revenue", "profit", "leads","lead_cpa", "max_lead_cpa", "sales", "sale_cpa","max_sale_cpa","epc"]].to_dict("records"))

print(json_final_result)

