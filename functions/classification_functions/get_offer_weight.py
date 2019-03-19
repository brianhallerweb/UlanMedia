from config.config import *
import json
import sys
import os
import re
import pandas as pd

import pprint
pp=pprint.PrettyPrinter(indent=2)
# you are making this obsolete on 3/19 so you will probably be able to delete
# it soon

# how offers work
# each campaign has a flow with offers
# when a user clicks on an ad, they get sent into the flow that matches their
# country and language. 
# that flow probabalistically determines which offer they are sent to
# The question is how to set the probabilities? You want to show users the
# offers they are most likely to buy. 

# how offer classification will work
# The question is how to set the weight of an offer inside a flow inside a
# campaign. 
# Mike's offers don't generate enough data inside each campaign and flow to
# decide.
# So we have to also look at the performance of offers across all campaigns

# parent vs child offers
# every offer is tailored to a country (eg Profit Formula DE)
# the parent offer is country independent (eg Profit Formula)
# the child offer is country dependent (eg Profit Formula DE)

#####################################
# 1. create_offers_for_each_flow_rule_dataset

def create_offers_for_each_flow_rule_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ################################################
    # the "data" dataset is structured like this:
    # campaign_id: child_offer_id {
    #                             offer data (campaign name, campaign id, clicks,
    #                             cost, profit, conversions, offer flow, offer
    #                             id, offer name)
    #                             }
    ################################################
    # make a list of flow rules
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


    return offers_for_each_flow_rule

offers_for_each_flow_rule = create_offers_for_each_flow_rule_dataset("oneeighty")

###################################
# 2. create_p_offers_gpr_lookup

def find_p_offer_rank(p_offers_gpr_lookup):
    unordered_p_offers = [] 
    for p_offer in p_offers_gpr_lookup:
        unordered_p_offers.append({"p_offer_name": p_offer, "profit":
            p_offers_gpr_lookup[p_offer]["profit"]})

    df = pd.DataFrame(unordered_p_offers)
    df = df.sort_values("profit")
    return list(df["p_offer_name"])

def create_p_offers_gpr_lookup(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ################################################
    # the "data" dataset is structured like this:
    # campaign_id: child_offer_id {
    #                             offer data (campaign name, campaign id, clicks,
    #                             cost, profit, conversions, offer flow, offer
    #                             id, offer name)
    #                             }
    ################################################

    c_offers_for_all_flow_rules = {"metadata": metadata, "data": {}}   
    for campaign in data:
        for offer in data[campaign]:
            if offer in c_offers_for_all_flow_rules["data"]:
                c_offers_for_all_flow_rules["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                c_offers_for_all_flow_rules["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                c_offers_for_all_flow_rules["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                c_offers_for_all_flow_rules["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 
                c_offers_for_all_flow_rules["data"][offer]["revenue"] += data[campaign][offer]["revenue"] 
            else:
                c_offers_for_all_flow_rules["data"][offer] = {
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
    for offer in c_offers_for_all_flow_rules["data"].values():
        p_offer_name = offer["p_offer_name"]
        if p_offer_name in p_offers_gpr_lookup:
            p_offers_gpr_lookup[p_offer_name]["profit"] += offer["profit"]
        else:
            p_offers_gpr_lookup[p_offer_name] = {"profit": offer["profit"]}

    ordered_p_offers = find_p_offer_rank(p_offers_gpr_lookup) 

    for i in range(0, len(ordered_p_offers)):
        p_offer_name = ordered_p_offers[i]
        p_offers_gpr_lookup[p_offer_name]["rank"] = i + 1 

    
    for p_offer in p_offers_gpr_lookup.values():
        p_offer["gpr"] = round((p_offer["rank"] ** 7) / (100000000))

    return p_offers_gpr_lookup

oneeighty_p_offers_gpr_lookup = create_p_offers_gpr_lookup("oneeighty")

##################################
# 3. Add roi cvr and gpr to offers_for_each_flow_rule

def add_stats_to_offers_for_each_flow_rule(offers_for_each_flow_rule, p_offers_gpr_lookup):
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

    return offers_for_each_flow_rule

offers_for_each_flow_rule = add_stats_to_offers_for_each_flow_rule(offers_for_each_flow_rule, oneeighty_p_offers_gpr_lookup)

###############################
# 4. Calculate the total score of each offer
# total_score = roi_score + cvr_score + gpr

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


def add_total_score_to_offers_for_each_flow_rule(offers_for_each_flow_rule):
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

    return offers_for_each_flow_rule



offers_for_each_flow_rule = add_total_score_to_offers_for_each_flow_rule(offers_for_each_flow_rule)

####################################

# 5. Calculate the weight of each offer

def add_weight_to_offers_for_each_flow_rule(offers_for_each_flow_rule):
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

    return offers_for_each_flow_rule

offers_for_each_flow_rule = add_weight_to_offers_for_each_flow_rule(offers_for_each_flow_rule)

#################################
# 6. create a function that gives an offers weight

def get_offer_weight(flow_rule, offer_id):
    return offers_for_each_flow_rule[flow_rule][offer_id]["weight"]

# weight = get_offer_weight("(bin: unitedKingdom - English)", "0343f17c-7539-4471-ad96-c09328ca0d88")

# pp.pprint(weight)

#################
# game plan

# make a dataset that has key = flow rule and value = offer_id
# for each offer_id, calculate an roi, cvr, and lookup the gpr, then sum
# them into a total score
# Then calculate child offer weight 
# Save the weight into the offers for all flow rule dataset

# You will have a dictionary that can act as a "weight" lookup given a
# flow_rule and an offer_id
# You will use this lookup to add a weight column to offers_for_all_flow_rules

# classification of bad offers seems to be a separate task


