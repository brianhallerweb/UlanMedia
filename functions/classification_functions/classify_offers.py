from config.config import *
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

# 2/6 You need to fix the regex for finding parent offers. The problem is
# things like Bitcoin Compass brazil PT
# Mike says there are only a few offers that have the "brazil" part so you can
# take that knowledge into account when doing the regex
# the other stuff like "a" instead of "A" are just typos that mike can fix
# Also ignore the 404 offer
# Then you will just proceed with the step after the ordering by total profit



def create_offers_for_all_campaigns_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_all_campaigns = {"metadata": metadata, "data": {}}   
    for campaign in data:
        for offer in data[campaign]:
            if offer in offers_for_all_campaigns["data"]:
                offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 

            else:
                offers_for_all_campaigns["data"][offer] = {
                                                          "offerName": data[campaign][offer]["offerName"],
                                                          "offerID": data[campaign][offer]["offerID"],
                                                          "offerFlow": data[campaign][offer]["offerFlow"],
                                                          "clicks": data[campaign][offer]["clicks"],
                                                           "cost": data[campaign][offer]["cost"],
                                                           "profit": data[campaign][offer]["profit"], 
                                                           "conversions": data[campaign][offer]["conversions"]
                                                          }

    pattern = re.compile(r'(.*) ([A-Z]+)')

    parent_offers_for_all_campaigns = {}
    for offer in offers_for_all_campaigns["data"].values():
        if offer["offerName"] == "404":
            continue
        else:
            res = list(pattern.findall(offer["offerName"])[0])
            parent_offer = res[0]
            if parent_offer in parent_offers_for_all_campaigns:
                parent_offers_for_all_campaigns[parent_offer]["total_profit"] += offer["profit"]
            else:
                parent_offers_for_all_campaigns[parent_offer] = {"total_profit": offer["profit"]}
    
    # Now parent_offers is roughtly a dict of parent offers with their total
    # profits.


    ordered_parent_offers = find_parent_offer_rank(parent_offers_for_all_campaigns) 

    for i in range(0, len(ordered_parent_offers)):
        offer_name = ordered_parent_offers[i]
        parent_offers_for_all_campaigns[offer_name]["rank"] = i + 1 
        

    # now you have all the parent offers with their total profit and their rank
    # in terms of profitability (1 is least profitable)
    # it looks like this:
    # { '1k Daily Profit': {'rank': 26, 'total_profit': 12796.84119},
    # '30 Day Challenge': {'rank': 22, 'total_profit': 4562.165930000001},
    # .
    # .
    # }
 
    ordered_parent_offers_for_all_campaigns = parent_offers_for_all_campaigns
    pp.pprint(ordered_parent_offers)
    pp.pprint(ordered_parent_offers_for_all_campaigns)

                

#########################    
# helper function
import pandas as pd

def find_parent_offer_rank(parent_offers_for_all_campaigns):
    unordered_parent_offers = [] 
    for parent_offer in parent_offers_for_all_campaigns:
        unordered_parent_offers.append({"parent_offer": parent_offer, "total_profit":
            parent_offers_for_all_campaigns[parent_offer]["total_profit"]})

    df = pd.DataFrame(unordered_parent_offers)
    df = df.sort_values("total_profit")
    return list(df["parent_offer"])

#################
# call the function
create_offers_for_all_campaigns_dataset("oneeighty")                
