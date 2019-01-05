from config.config import *
import json
import os
import sys
from functions.misc.get_campaign_sets import get_campaign_sets 

def create_campaigns_for_one_offer_dataset(date_range, offer_id):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_offer = {"metadata": metadata, "data": []}   
    for campaign in data:
        for offer in data[campaign]:
            if offer == offer_id:
                campaigns_for_one_offer["data"].append(data[campaign][offer])

    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["name"]
    
    for campaign in campaigns_for_one_offer["data"]:
        name = campaigns_lookup[campaign["campaignID"]]
        campaign["campaignName"] = name


    with open(f"../../data/campaigns_for_one_offer/{offer_id}_{date_range}_campaigns_for_one_offer_dataset.json", "w") as file:
        json.dump(campaigns_for_one_offer, file)
    
    return json.dumps(campaigns_for_one_offer)

