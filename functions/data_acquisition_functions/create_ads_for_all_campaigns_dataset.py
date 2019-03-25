from config.config import *
import json
import os
import sys
import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_ads_for_all_campaigns_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    # create a new dictionary with keys = image
    ads_data_by_ad_image = {"metadata": metadata, "data": {}}   
    for ad in data.values():
        image = ad["for_all_campaigns"]["image"]
        ads_data_by_ad_image["data"][image] = ad["for_all_campaigns"] 

    with open(f"../../data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json", "w") as file:
        json.dump(ads_data_by_ad_image, file)
    
    return json.dumps(ads_data_by_ad_image)


    









