from config.config import *
import json
import sys
import os


def create_campaigns_for_one_ad_dataset(ad_image, date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_ad = {"metadata": metadata, "data": []}   

    for ad in data.values():
        image = ad["image"]
        if image == ad_image:
            campaigns_for_one_ad["data"].append(ad)

    with open(f"../../data/campaigns_for_one_ad/{ad_image}_{date_range}_campaigns_for_one_ad_dataset.json", "w") as file:
        json.dump(campaigns_for_one_ad, file)

    return json.dumps(campaigns_for_one_ad)


    









