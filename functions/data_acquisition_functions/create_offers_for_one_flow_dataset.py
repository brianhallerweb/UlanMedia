from config.config import *
import json
import sys
import os

def create_offers_for_one_flow_dataset(date_range, flow):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_one_flow = {"metadata": metadata, "data": {} }   

    for campaign in data:
        for offer in data[campaign]:
            if data[campaign][offer]["offerFlow"] == flow:
                if offer in offers_for_one_flow["data"]:
                    offers_for_one_flow["data"][offer]["clicks"] += data[campaign][offer]["clicks"] 
                    offers_for_one_flow["data"][offer]["cost"] += data[campaign][offer]["cost"] 
                    offers_for_one_flow["data"][offer]["profit"] += data[campaign][offer]["profit"] 
                    offers_for_one_flow["data"][offer]["conversions"] += data[campaign][offer]["conversions"] 
                else:
                    offers_for_one_flow["data"][offer] = data[campaign][offer]

    with open(f"../../data/offers_for_one_flow/{flow}_{date_range}_offers_for_one_flow_dataset.json", "w") as file:
        json.dump(offers_for_one_flow, file)
    
    return json.dumps(offers_for_one_flow)


