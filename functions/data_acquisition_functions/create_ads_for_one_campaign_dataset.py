from config.config import *
import json
import sys


def create_ads_for_one_campaign_dataset(vol_id, date_range):

    with open(f'/home/bsh/Documents/UlanMedia/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        ads = json.load(file)

    ads_for_one_campaign = []   
    for ad in ads.values():
        campaign = ad["vol_id"]
        if campaign == vol_id:
            ads_for_one_campaign.append(ad)

    with open(f"../../data/ads_for_one_campaign/{vol_id}_{date_range}_ads_for_one_campaign_dataset.json", "w") as file:
        json.dump(ads_for_one_campaign, file)


    









