from config.config import *
import json
import sys
import os

def create_offers_for_all_flow_rules_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_all_flow_rules = {"metadata": metadata, "data": {}}   
    for offer in data:
        if offer in offers_for_all_flow_rules["data"]:
            offers_for_all_flow_rules["data"][offer]["clicks"] += data[offer]["clicks"] 
            offers_for_all_flow_rules["data"][offer]["cost"] += data[offer]["cost"] 
            offers_for_all_flow_rules["data"][offer]["profit"] += data[offer]["profit"] 
            offers_for_all_flow_rules["data"][offer]["conversions"] += data[offer]["conversions"] 

        else:
            offers_for_all_flow_rules["data"][offer] = {
                                                      "offer_name": data[offer]["offer_name"],
                                                      "offer_id": data[offer]["offer_id"],
                                                      "flow_rule": data[offer]["flow_rule"],
                                                      "clicks": data[offer]["clicks"],
                                                      "cost": data[offer]["cost"],
                                                      "profit": data[offer]["profit"], 
                                                      "conversions": data[offer]["conversions"]
                                                      }
    

    with open(f"../../data/offers_for_all_flow_rules/{date_range}_offers_for_all_flow_rules_dataset.json", "w") as file:
        json.dump(offers_for_all_flow_rules, file)
    
    return json.dumps(offers_for_all_flow_rules)

# def create_offers_for_all_campaigns_dataset(date_range):

    # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        # json_file = json.load(file)

    # metadata = json_file["metadata"]
    # data = json_file["data"]

    # offers_for_all_campaigns = {"metadata": metadata, "data": {}}   
    # for campaign in data:
        # for offer in data[campaign]:
            # if offer in offers_for_all_campaigns["data"]:
                # offers_for_all_campaigns["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                # offers_for_all_campaigns["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                # offers_for_all_campaigns["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                # offers_for_all_campaigns["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 

            # else:
                # offers_for_all_campaigns["data"][offer] = {
                                                          # "offerName": data[campaign][offer]["offerName"],
                                                          # "offerID": data[campaign][offer]["offerID"],
                                                          # "offerFlow": data[campaign][offer]["offerFlow"],
                                                          # "clicks": data[campaign][offer]["clicks"],
                                                           # "cost": data[campaign][offer]["cost"],
                                                           # "profit": data[campaign][offer]["profit"], 
                                                           # "conversions": data[campaign][offer]["conversions"]
                                                          # }
        

    # with open(f"../../data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json", "w") as file:
        # json.dump(offers_for_all_campaigns, file)
    
    # return json.dumps(offers_for_all_campaigns)
