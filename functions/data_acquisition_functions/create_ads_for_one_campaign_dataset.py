from config.config import *
import json
import sys
import os


def create_ads_for_one_campaign_dataset(vol_id, date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    ads_for_one_campaign = {"metadata": metadata, "data": []}   

    for ad in data.values():
        campaign = ad["vol_id"]
        if campaign == vol_id:
            ads_for_one_campaign["data"].append(ad)

    with open(f"../../data/ads_for_one_campaign/{vol_id}_{date_range}_ads_for_one_campaign_dataset.json", "w") as file:
        json.dump(ads_for_one_campaign, file)

    return json.dumps(ads_for_one_campaign)


    









