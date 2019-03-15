from config.config import *
import json
import sys
import os

def create_offers_for_one_flow_rule_dataset(date_range, flow_rule):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_one_flow_rule = {"metadata": metadata, "data": {} }   

    for offer in data:
        if data[offer]["flow_rule"] == flow_rule:
            if offer in offers_for_one_flow_rule["data"]:
                offers_for_one_flow_rule["data"][offer]["clicks"] += data[offer]["clicks"] 
                offers_for_one_flow_rule["data"][offer]["cost"] += data[offer]["cost"] 
                offers_for_one_flow_rule["data"][offer]["profit"] += data[offer]["profit"] 
                offers_for_one_flow_rule["data"][offer]["revenue"] += data[offer]["revenue"] 
                offers_for_one_flow_rule["data"][offer]["conversions"] += data[offer]["conversions"] 
            else:
                offers_for_one_flow_rule["data"][offer] = data[offer]

    with open(f"../../data/offers_for_one_flow_rule/{flow_rule}_{date_range}_offers_for_one_flow_rule_dataset.json", "w") as file:
        json.dump(offers_for_one_flow_rule, file)
    
    return json.dumps(offers_for_one_flow_rule)


