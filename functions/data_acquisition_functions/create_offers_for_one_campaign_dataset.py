from config.config import *
import json
import sys
import os

def create_offers_for_one_campaign_dataset(date_range, vol_id):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    offers_for_one_campaign = {"metadata": metadata, "data": [] }   

    for offer in data[vol_id]:
        offers_for_one_campaign["data"].append(data[vol_id][offer])

    with open(f"../../data/offers_for_one_campaign/{vol_id}_{date_range}_offers_for_one_campaign_dataset.json", "w") as file:
        json.dump(offers_for_one_campaign, file)
    
    return json.dumps(offers_for_one_campaign)


