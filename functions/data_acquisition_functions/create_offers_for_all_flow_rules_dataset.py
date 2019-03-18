from config.config import *
import json
import sys
import os

from functions.classification_functions.get_offer_weight import get_offer_weight

def create_offers_for_all_flow_rules_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_all_flow_rules = {"metadata": metadata, "data": {}}   

    for campaign in data:
        for offer in data[campaign]:
            if offer in offers_for_all_flow_rules["data"]:
                offers_for_all_flow_rules["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                offers_for_all_flow_rules["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                offers_for_all_flow_rules["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                offers_for_all_flow_rules["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 
                offers_for_all_flow_rules["data"][offer]["revenue"] += data[campaign][offer]["revenue"] 
            else:
                offers_for_all_flow_rules["data"][offer] = {
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
                                                          "weight": get_offer_weight(data[campaign][offer]["flow_rule"],data[campaign][offer]["offer_id"])
                                                          }
    

    with open(f"../../data/offers_for_all_flow_rules/{date_range}_offers_for_all_flow_rules_dataset.json", "w") as file:
        json.dump(offers_for_all_flow_rules, file)
    
    return json.dumps(offers_for_all_flow_rules)

