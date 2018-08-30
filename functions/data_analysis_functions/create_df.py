import pandas as pd
import numpy as np

def create_df(data, output_html):
    df = pd.DataFrame(data)
    df["max_lead_cpa"] = df["max_lead_cpa"].astype("float64")
    df["max_sale_cpa"] = df["max_sale_cpa"].astype("float64")
    df["epc"] = round(df["revenue"] / df["clicks"], 2)
    df["lead_cpa"] = round(df["cost"] / df["leads"], 2)
    df["sale_cpa"] = round(df["cost"] / df["sales"], 2)
    df["profit"] = df["revenue"] - df["cost"]

    # profit < - max_sale_cpa 
    c1 = df["profit"] < -df["max_sale_cpa"]
    result1 = df[c1]
    result1["c1"] = "yes" 

    # clicks > 1000 and leads = 0
    c2 = (df["clicks"] > 1000) & (df["leads"] == 0)
    result2 = df[c2]
    result2["c2"] = "yes" 
    
    # cost > 0.3*maxSaleCPA and leadCPA > 2*maxLeadCPA 
    c3 = (df["cost"] > 0.3*df["max_sale_cpa"]) & (df["lead_cpa"] >
    2*df["max_lead_cpa"])
    result3 = df[c3] 
    result3["c3"] = "yes"

    # cost > 0.5*maxSaleCPA and leadCPA > 1.5*maxLeadCPA    
    c4 = (df["cost"] > 0.5*df["max_sale_cpa"]) & (df["lead_cpa"] >
    1.5*df["max_lead_cpa"])
    result4 = df[c4]
    result4["c4"] = "yes"

    # cost > 2*maxSaleCPA and leadCPA > maxLeadCPA 
    c5 = (df["cost"] > 2*df["max_sale_cpa"]) & (df["lead_cpa"] >
        df["max_lead_cpa"])
    result5 = df[c5]
    result5["c5"]="yes"
    
    # merge all the tables
    result12 = result1.merge(result2, how="outer", on=["name", "clicks", "cost", "imps", "leads",
    "max_lead_cpa", "max_sale_cpa", "epc", "mgid_id", "revenue", "sales",
    "vol_id", "lead_cpa", "sale_cpa", "profit"])

    result123 = result12.merge(result3, how="outer", on=["name", "clicks", "cost", "imps", "leads",
    "max_lead_cpa", "max_sale_cpa", "epc", "mgid_id", "revenue", "sales",
    "vol_id", "lead_cpa", "sale_cpa", "profit"])

    result1234 = result123.merge(result4, how="outer", on=["name", "clicks", "cost", "imps", "leads",
    "max_lead_cpa", "max_sale_cpa", "epc", "mgid_id", "revenue", "sales",
    "vol_id", "lead_cpa", "sale_cpa", "profit"])

    result12345 = result1234.merge(result5, how="outer", on=["name", "clicks", "cost", "imps", "leads",
    "max_lead_cpa", "max_sale_cpa", "epc", "mgid_id", "revenue", "sales",
    "vol_id", "lead_cpa", "sale_cpa", "profit"])

    
    final_result = result12345 
    final_result = final_result.replace([np.inf, -np.inf], 0)
    final_result["c1"] = final_result["c1"].replace(np.nan, "no")
    final_result["c2"] = final_result["c2"].replace(np.nan, "no")
    final_result["c3"] = final_result["c3"].replace(np.nan, "no")
    final_result["c4"] = final_result["c4"].replace(np.nan, "no")
    final_result["c5"] = final_result["c5"].replace(np.nan, "no")
    final_result["sort"] = final_result["name"].str[4:]
    final_result = final_result.sort_values("sort")
    final_result[["name", "clicks", "cost","revenue", "profit", "leads",
        "lead_cpa", "max_lead_cpa", "sales",
        "sale_cpa","max_sale_cpa","epc", "c1", "c2", "c3", "c4",
        "c5"]].to_html(f"../../dashboard/reports/{output_html}.html")

   

