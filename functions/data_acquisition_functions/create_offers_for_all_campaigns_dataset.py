from config.config import *
import json
import sys


def create_offers_for_all_campaigns_dataset(date_range):

    with open(f'/home/bsh/Documents/UlanMedia/data/offers/{date_range}_offers_dataset.json', 'r') as file:
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
        

    with open(f"../../data/offers_for_all_campaigns/{date_range}_offers_for_all_campaigns_dataset.json", "w") as file:
        json.dump(offers_for_all_campaigns, file)
    
    return json.dumps(offers_for_all_campaigns)

