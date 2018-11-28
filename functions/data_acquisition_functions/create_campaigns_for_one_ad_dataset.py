from config.config import *
import json
import sys


def create_campaigns_for_one_ad_dataset(ad_image, date_range):

    with open(f'/home/bsh/Documents/UlanMedia/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        ads = json.load(file)

    campaigns = []   
    for ad in ads.values():
        image = ad["image"]
        if image == ad_image:
            campaigns.append(ad)

    with open(f"../../data/campaigns_for_one_ad/{ad_image}_{date_range}_campaigns_for_one_ad_dataset.json", "w") as file:
        json.dump(campaigns, file)


    









