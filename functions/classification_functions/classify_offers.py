from config.config import *
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

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

def create_parent_offers_for_all_campaigns_dataset(date_range):

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

    child_offers_for_all_campaigns = {"metadata": metadata, "data": {}}   
    for campaign in data:
        for offer in data[campaign]:
            if offer in child_offers_for_all_campaigns["data"]:
                child_offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                child_offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                child_offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                child_offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 

            else:
                child_offers_for_all_campaigns["data"][offer] = {
                                                          "offerName": data[campaign][offer]["offerName"],
                                                          "offerID": data[campaign][offer]["offerID"],
                                                          "offerFlow": data[campaign][offer]["offerFlow"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"], 
                                                           "conversions": data[campaign][offer]["conversions"]
                                                          }
    ################################################
    # At this point child_offers_for_all_campaigns["data"] is structured like this:
    # child_offer_id1 {
    #                 offer data (clicks, cost, profit, conversions, offer flow, offer
    #                 id, offer name)
    #                 }, 
    # child_offer_id2 {
    #                 more offer data 
    #                 } 
    ################################################

    country_list = ["spain", "latam", "brazil", "portugal"]
    tier_list = ["tier1", "tier3"]

    parent_offers_for_all_campaigns = {}
    for offer in child_offers_for_all_campaigns["data"].values():
        if offer["offerName"] == "404":
            continue
        else:
            offer_words = offer["offerName"].split(" ")
            # remove the country code at the end (eg. DE)
            offer_words.pop()
            # remove the country name if there is one (eg. spain)
            if offer_words[len(offer_words) - 1] in country_list:
                offer_words.pop()
            # remove the tier if there is one (eg. tier1)
            if offer_words[len(offer_words) - 1] in tier_list:
                offer_words.pop()
            parent_offer = " ".join(offer_words)
            if parent_offer in parent_offers_for_all_campaigns:
                parent_offers_for_all_campaigns[parent_offer]["profit"] += offer["profit"]
                parent_offers_for_all_campaigns[parent_offer]["clicks"] += offer["clicks"]
                parent_offers_for_all_campaigns[parent_offer]["cost"] += offer["cost"]
                parent_offers_for_all_campaigns[parent_offer]["conversions"] += offer["conversions"]
            else:
                parent_offers_for_all_campaigns[parent_offer] = {"profit": offer["profit"],
                        "clicks": offer["clicks"], "cost": offer["cost"], 
                        "parent_offer": parent_offer, "conversions":
                        offer["conversions"]}

    
    ordered_parent_offers = find_parent_offer_rank(parent_offers_for_all_campaigns) 

    for i in range(0, len(ordered_parent_offers)):
        offer_name = ordered_parent_offers[i]
        parent_offers_for_all_campaigns[offer_name]["rank"] = i + 1 

    # now parent_offers_for_all_campaigns is a dictionary of dictionaries that
    # looks like this:
    # { '1k Daily Profit': {'rank': 26, 'total_profit': 12796.84119},
    # '30 Day Challenge': {'rank': 22, 'total_profit': 4562.165930000001},
    # .
    # .
    # }
    
    for parent_offer in parent_offers_for_all_campaigns.values():
        parent_offer["gpr"] = round((parent_offer["rank"] ** 7) / (100000000))

    pp.pprint(parent_offers_for_all_campaigns)
 

                

#########################    
# helper function
import pandas as pd

def find_parent_offer_rank(parent_offers_for_all_campaigns):
    unordered_parent_offers = [] 
    for parent_offer in parent_offers_for_all_campaigns:
        unordered_parent_offers.append({"parent_offer": parent_offer, "profit":
            parent_offers_for_all_campaigns[parent_offer]["profit"]})

    df = pd.DataFrame(unordered_parent_offers)
    df = df.sort_values("profit")
    return list(df["parent_offer"])



def create_child_offers_for_all_campaigns_dataset(date_range):

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

    child_offers_for_all_campaigns = {"metadata": metadata, "data": {}}   
    for campaign in data:
        for offer in data[campaign]:
            if offer in child_offers_for_all_campaigns["data"]:
                child_offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                child_offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                child_offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                child_offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 

            else:
                child_offers_for_all_campaigns["data"][offer] = {
                                                          "offerName": data[campaign][offer]["offerName"],
                                                          "offerID": data[campaign][offer]["offerID"],
                                                          "offerFlow": data[campaign][offer]["offerFlow"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"], 
                                                           "conversions": data[campaign][offer]["conversions"]
                                                          }
    ################################################
    # At this point child_offers_for_all_campaigns["data"] is structured like this:
    # child_offer_id1 {
    #                 offer data (clicks, cost, profit, conversions, offer flow, offer
    #                 id, offer name)
    #                 }, 
    # child_offer_id2 {
    #                 more offer data 
    #                 } 
    ################################################
    pp.pprint(child_offers_for_all_campaigns)


#################
create_child_offers_for_all_campaigns_dataset("oneeighty")                
