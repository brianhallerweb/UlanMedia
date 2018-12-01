from config.config import *
import json


def create_ads_for_all_campaigns_dataset(date_range):

    with open(f'/home/bsh/Documents/UlanMedia/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        ads = json.load(file)

    # create a new dictionary with keys = image
    ads_data_by_ad_image = {}   
    for ad in ads.values():
        image = ad["image"]
        if image in ads_data_by_ad_image:
            ads_data_by_ad_image[image]["clicks"] += ad["clicks"] 
            ads_data_by_ad_image[image]["conversions"] += ad["conversions"] 
            ads_data_by_ad_image[image]["cost"] += ad["cost"] 
            ads_data_by_ad_image[image]["revenue"] += ad["revenue"] 
        else:
            ads_data_by_ad_image[image] = ad


    with open(f"../../data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json", "w") as file:
        json.dump(ads_data_by_ad_image, file)


    









