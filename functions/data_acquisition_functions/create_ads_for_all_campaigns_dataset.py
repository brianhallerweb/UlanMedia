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
        image = ad["image"]
        if image in ads_data_by_ad_image:
            ads_data_by_ad_image["data"][image]["clicks"] += ad["clicks"] 
            ads_data_by_ad_image["data"][image]["conversions"] += ad["conversions"] 
            ads_data_by_ad_image["data"][image]["cost"] += ad["cost"] 
            ads_data_by_ad_image["data"][image]["revenue"] += ad["revenue"] 
        else:
            ads_data_by_ad_image["data"][image] = ad

    for ad_image in ads_data_by_ad_image["data"].values():
        clicks = ad_image["clicks"]
        cost = ad_image["cost"]
        revenue = ad_image["revenue"]
        profit = revenue - cost
        conversions = ad_image["conversions"]

        ad_image["profit"] = profit
        if cost == 0:
            ad_image["roi"] = 0
        else:
            ad_image["roi"] = profit/cost
        if clicks == 0:
            ad_image["epc"] = 0
        else:
            ad_image["epc"] = profit/clicks
        if clicks == 0:
            ad_image["cvr"] = 0
        else:
            ad_image["cvr"] = conversions/clicks

    for ad_image in ads_data_by_ad_image["data"].values():
        clicks = ad_image["clicks"]
        profit = ad_image["profit"]
        revenue = ad_image["revenue"]
        epc = ad_image["epc"]
        roi = ad_image["roi"]
        cvr = ad_image["cvr"]
        conversions = ad_image["conversions"]
        if revenue > 0:
            ad_image["global_rank"] = clicks * profit * epc * roi
        else:
            if cvr == 0:
                ad_image["global_rank"] = 0
            else:
                ad_image["global_rank"] = clicks * profit / cvr
            


        pp.pprint(ad_image)

    sys.exit()


    with open(f"../../data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json", "w") as file:
        json.dump(ads_data_by_ad_image, file)
    
    return json.dumps(ads_data_by_ad_image)


    









