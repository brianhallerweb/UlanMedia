from config.config import *
from datetime import datetime
import json
import sys
import re
import os
from functions.classification_functions.classify_offer_for_all_campaigns import classify_offer_for_all_campaigns
import pandas as pd

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_gprs_for_each_p_offer_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json', 'r') as file:
        json_file = json.load(file)
    offers_for_each_flow_rule = json_file["data"]

    #####################################

    gprs_for_each_p_offer = {}   

    for flow_rule in offers_for_each_flow_rule:
        for offer in offers_for_each_flow_rule[flow_rule]:
            p_offer_name = offers_for_each_flow_rule[flow_rule][offer]["p_offer_name"]
            gpr = offers_for_each_flow_rule[flow_rule][offer]["gpr"]
            profit = offers_for_each_flow_rule[flow_rule][offer]["profit"]
            rank = offers_for_each_flow_rule[flow_rule][offer]["total_score_rank"]
            if p_offer_name in gprs_for_each_p_offer:
                gprs_for_each_p_offer[p_offer_name]["profit"] += profit
            else:
                gprs_for_each_p_offer[p_offer_name] = {"name": p_offer_name,
                        "gpr": gpr, "profit": profit, "rank": rank, "formula":
                        "will fill in later"}

    for p_offer_name in gprs_for_each_p_offer:
        rounded_profit = round(gprs_for_each_p_offer[p_offer_name]["profit"], 2)
        gprs_for_each_p_offer[p_offer_name]["profit"] = rounded_profit

    gprs_for_each_p_offer_list = []
    for p_offer_name in gprs_for_each_p_offer:
        gprs_for_each_p_offer_list.append(gprs_for_each_p_offer[p_offer_name])

    gprs_for_each_p_offer_list = pd.DataFrame(gprs_for_each_p_offer_list)
    gprs_for_each_p_offer_list = gprs_for_each_p_offer_list.sort_values("rank", ascending=False)
    
    return json.dumps(gprs_for_each_p_offer_list[["rank", "profit", "name",
        "gpr", "formula"]].to_dict("records"))


