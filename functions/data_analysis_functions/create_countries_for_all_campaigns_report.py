import sys
import os
import json
import pandas as pd
import numpy as np


def create_countries_for_all_campaigns_report(date_range, c1_input, c2_input,
        c3_input, c1Value_input, c2Value_input, c3Value_input):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/countries_for_all_campaigns/{date_range}_countries_for_all_campaigns_dataset.json', 'r') as file:
         json_file = json.load(file)
    
    data = json_file["data"]
    
    df = pd.DataFrame(data)
    df["cost"] = round(df["cost"], 2)
    df["profit"] = round(df["revenue"] - df["cost"], 2)
    df["lead_cvr"] = round((df["leads"] / df["clicks"]) * 100,
            2)
    df["epc"] = (df["revenue"] / df["clicks"]).round(3)
    df["cpl"] = round(df["cost"] / df["leads"], 2)
    df["cps"] = round(df["cost"] / df["sales"], 2)
    df["cpc"] = round(df["cost"] / df["clicks"], 2)
    df["epl"] = round(df["revenue"] / df["leads"], 2)
    df["eps"] = round(df["revenue"] / df["sales"], 2)
    df["roi"] = round((df["profit"] / df["cost"])*100, 2)
    
    c1 = df["classification"] == c1Value_input
    result1 = df[c1]
    
    c2 = df["cost"] >= float(c2Value_input)
    result2 = df[c2]
    
    c3 = df["profit"] <= -1 * float(c3Value_input)
    result3 = df[c3]
    
    conditions_args = [c1_input, c2_input, c3_input]
    conditions_dfs = [result1, result2, result3]
    
    final_result = None 
    for i in range(len(conditions_args)):
        if conditions_args[i] == True and final_result is None:
            final_result = conditions_dfs[i]
        elif conditions_args[i] == True:
            final_result = final_result.merge(conditions_dfs[i], how="inner",
            on=["country_name", "classification", "clicks", "cost", "conversions",
                "leads", "sales", "profit","revenue", "lead_cvr", "epc",
                "cpl", "cps", "cpc", "epl", "eps", "roi"] )
    
    if final_result is None:
        final_result = df
    
    final_result = final_result.replace([np.inf, -np.inf], "NaN")
    final_result = final_result.replace(np.nan, "NaN")
    final_result["sort"] = final_result["cost"]
    final_result = final_result.sort_values("sort", ascending=False)
    json_final_result = json.dumps(final_result[["country_name", "classification",
        "clicks", "cost", "conversions", "leads", "sales", "profit","revenue",
        "lead_cvr", "epc", "cpl", "cps", "cpc", "epl", "eps", "roi"]].to_dict("records"))
    
    return json_final_result
    
