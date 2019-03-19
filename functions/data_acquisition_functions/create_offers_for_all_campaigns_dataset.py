from config.config import *
from datetime import datetime
import json
import sys
import re
import os

def create_offers_for_all_campaigns_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_campaign/{date_range}_offers_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ######################################

    # 1. create_offers_for_each_flow_rule_dataset

    flow_rules = []
    for campaign in data:
        for offer in data[campaign]:
            if data[campaign][offer]["flow_rule"] in flow_rules:
                continue
            else:
                flow_rules.append(data[campaign][offer]["flow_rule"])

    offers_for_each_flow_rule = {}
    for flow_rule in flow_rules:
        offers_for_each_flow_rule[flow_rule] = {}

    for campaign in data:
        for offer in data[campaign]:
            flow_rule = data[campaign][offer]["flow_rule"]
            offers_for_each_flow_rule[flow_rule][offer] = {
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"], 
                                                           "conversions": data[campaign][offer]["conversions"],
                                                           "revenue": data[campaign][offer]["revenue"],
                                                          }

    # At this point, offers_for_each_flow_rule has been created
    #########################################
    
    # 2. create_p_offers_gpr_lookup

    # def find_p_offer_rank(p_offers_gpr_lookup):
    # unordered_p_offers = []
    # for p_offer in p_offers_gpr_lookup:
        # unordered_p_offers.append({"p_offer_name": p_offer, "profit":
            # p_offers_gpr_lookup[p_offer]["profit"]})

    # df = pd.DataFrame(unordered_p_offers)
    # df = df.sort_values("profit")
    # return list(df["p_offer_name"])

    c_offers_for_all_campaigns = {}

    for campaign in data:
        for offer in data[campaign]:
            if offer in c_offers_for_all_campaigns:
                c_offers_for_all_campaigns[offer]["clicks"] += data[campaign][offer]["clicks"]
                c_offers_for_all_campaigns[offer]["cost"] += data[campaign][offer]["cost"]
                c_offers_for_all_campaigns[offer]["profit"] += data[campaign][offer]["profit"]
                c_offers_for_all_campaigns[offer]["conversions"] += data[campaign][offer]["conversions"]
                c_offers_for_all_campaigns[offer]["revenue"] += data[campaign][offer]["revenue"]
            else:
                c_offers_for_all_campaigns[offer] = {
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"],
                                                           "conversions": data[campaign][offer]["conversions"],
                                                           "revenue": data[campaign][offer]["revenue"]
                                                          }

    p_offers_gpr_lookup = {}

    for offer in c_offers_for_all_campaigns.values():
        p_offer_name = offer["p_offer_name"]
        if p_offer_name in p_offers_gpr_lookup:
            p_offers_gpr_lookup[p_offer_name]["profit"] += offer["profit"]
        else:
            p_offers_gpr_lookup[p_offer_name] = {"profit": offer["profit"]}

    unordered_p_offers = []
    for p_offer in p_offers_gpr_lookup:
        unordered_p_offers.append({"p_offer_name": p_offer, "profit":
            p_offers_gpr_lookup[p_offer]["profit"]})

    df = pd.DataFrame(unordered_p_offers)
    df = df.sort_values("profit")
    list(df["p_offer_name"])
    ordered_p_offers = list(df["p_offer_name"])


    for i in range(0, len(ordered_p_offers)):
        p_offer_name = ordered_p_offers[i]
        p_offers_gpr_lookup[p_offer_name]["rank"] = i + 1


    for p_offer in p_offers_gpr_lookup.values():
        p_offer["gpr"] = round((p_offer["rank"] ** 7) / (100000000))


    # At this point, offers_for_each_flow_rule exists and you have a
    # p_offers_gpr_lookup dictionary which tells you the gpr  of each parent
    # offer

    ##################################

    # 3. Add roi cvr and gpr to offers_for_each_flow_rule

    for flow_rule in offers_for_each_flow_rule:
        for offer in offers_for_each_flow_rule[flow_rule]:
            profit = offers_for_each_flow_rule[flow_rule][offer]["profit"]
            cost = offers_for_each_flow_rule[flow_rule][offer]["cost"]
            if cost == 0:
                offers_for_each_flow_rule[flow_rule][offer]["roi"] = 0
            else:
                offers_for_each_flow_rule[flow_rule][offer]["roi"] = profit/cost

            conversions = offers_for_each_flow_rule[flow_rule][offer]["conversions"]
            clicks = offers_for_each_flow_rule[flow_rule][offer]["clicks"]
            if clicks == 0:
                offers_for_each_flow_rule[flow_rule][offer]["cvr"] = 0
            else:
                offers_for_each_flow_rule[flow_rule][offer]["cvr"] = conversions/clicks

            p_offer_name = offers_for_each_flow_rule[flow_rule][offer]["p_offer_name"]
            gpr = p_offers_gpr_lookup[p_offer_name]["gpr"]
            offers_for_each_flow_rule[flow_rule][offer]["gpr"] = gpr

    ###############################
    # 4. Calculate the total score of each offer (uses helper functions at the
    # bottom of this file)
    # total_score = roi_score + cvr_score + gpr

    for flow_rule in offers_for_each_flow_rule:
        for offer in offers_for_each_flow_rule[flow_rule]:
            roi = offers_for_each_flow_rule[flow_rule][offer]["roi"]
            cvr = offers_for_each_flow_rule[flow_rule][offer]["cvr"]
            gpr = offers_for_each_flow_rule[flow_rule][offer]["gpr"]

            roi_score = get_roi_score(roi)
            cvr_score = get_cvr_score(cvr)
            total_score = roi_score + cvr_score + gpr

            offers_for_each_flow_rule[flow_rule][offer]["roi_score"] = roi_score
            offers_for_each_flow_rule[flow_rule][offer]["cvr_score"] = cvr_score
            offers_for_each_flow_rule[flow_rule][offer]["total_score"] = total_score

    ####################################

    # 5. Calculate the weight of each offer

    for flow_rule in offers_for_each_flow_rule:
        total_flow_rule_score = 0
        for offer in offers_for_each_flow_rule[flow_rule]:
            total_flow_rule_score += offers_for_each_flow_rule[flow_rule][offer]["total_score"]
        for offer in offers_for_each_flow_rule[flow_rule]:
            total_score = offers_for_each_flow_rule[flow_rule][offer]["total_score"] 
            if total_flow_rule_score == 0:
                offers_for_each_flow_rule[flow_rule][offer]["weight"] = 0
            else:
                offers_for_each_flow_rule[flow_rule][offer]["weight"] = total_score / total_flow_rule_score * 100


    # At thie point, offers_for_each_flow_rule is a lookup dictionary to find
    # the weight of each offer. In the next step you will add that weight to
    # the offers_for_all_campaigns dataset
    ########################################

    # 6. Create the offers_for_all_campaigns dataset
 
    offers_for_all_campaigns = {"metadata": metadata, "data": {}}   

    for campaign in data:
        for offer in data[campaign]:
            if offer in offers_for_all_campaigns["data"]:
                offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 
                offers_for_all_campaigns["data"][offer]["revenue"] += data[campaign][offer]["revenue"] 
            else:
                offers_for_all_campaigns["data"][offer] = {
                                                          "offer_id": data[campaign][offer]["offer_id"],
                                                          "vol_offer_name": data[campaign][offer]["vol_offer_name"],
                                                          "offer_name": data[campaign][offer]["offer_name"],
                                                          "p_offer_name": data[campaign][offer]["p_offer_name"],
                                                          "c_offer_name": data[campaign][offer]["c_offer_name"],
                                                          "flow_rule": data[campaign][offer]["flow_rule"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                          "cost": data[campaign][offer]["cost"],
                                                          "profit": data[campaign][offer]["profit"], 
                                                          "revenue": data[campaign][offer]["revenue"], 
                                                          "conversions": data[campaign][offer]["conversions"],
                                                          "weight": get_offer_weight(offers_for_each_flow_rule, data[campaign][offer]["flow_rule"],data[campaign][offer]["offer_id"])
                                                          }
    

    with open(f"../../data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json", "w") as file:
        json.dump(offers_for_all_campaigns, file)
    
    return json.dumps(offers_for_all_campaigns)

#################################
# helper functions
def get_roi_score(roi):
    if roi >= 5:
        return 20
    elif roi >= 4:
        return 16
    elif roi >= 3:
        return 14
    elif roi >= 2:
        return 12
    elif roi >= 1:
        return 10
    elif roi >= 0:
        return 5 
    else:
        return 0 

def get_cvr_score(cvr):
    if cvr >= .02:
        return 8
    elif cvr >= .015:
        return 7 
    elif cvr >= .010:
        return 5 
    elif cvr >= .006:
        return 4 
    elif cvr >= .005:
        return 3 
    elif cvr >= .003:
        return 2 
    elif cvr >= .002:
        return 1 
    # this looks like a mistake but it is what was in mikes example php
    elif cvr >= .001:
        return 1 
    else:
        return 0 

def get_offer_weight(offers_for_each_flow_rule, flow_rule, offer_id):
    return offers_for_each_flow_rule[flow_rule][offer_id]["weight"]
