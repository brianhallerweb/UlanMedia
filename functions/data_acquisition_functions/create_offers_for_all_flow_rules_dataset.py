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
            offers_for_all_flow_rules["data"][offer]["revenue"] += data[offer]["revenue"] 
        else:
            offers_for_all_flow_rules["data"][offer] = {
                                                      "offer_id": data[offer]["offer_id"],
                                                      "vol_offer_name": data[offer]["vol_offer_name"],
                                                      "offer_name": data[offer]["offer_name"],
                                                      "p_offer_name": data[offer]["p_offer_name"],
                                                      "c_offer_name": data[offer]["c_offer_name"],
                                                      "flow_rule": data[offer]["flow_rule"],
                                                      "clicks": data[offer]["clicks"],
                                                      "cost": data[offer]["cost"],
                                                      "profit": data[offer]["profit"], 
                                                      "revenue": data[offer]["revenue"], 
                                                      "conversions": data[offer]["conversions"]
                                                      }
    

    with open(f"../../data/offers_for_all_flow_rules/{date_range}_offers_for_all_flow_rules_dataset.json", "w") as file:
        json.dump(offers_for_all_flow_rules, file)
    
    return json.dumps(offers_for_all_flow_rules)

