from config.config import *
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.classification_functions.classify_p_and_c_ads import classify_p_and_c_ads
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.get_campaign_sets import get_campaign_sets
import sys
import json
import os

import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_complete_ads_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        json_file = json.load(file)


    complete_ads = {"metadata": {"vol_start_date": json_file["metadata"]["vol_start_date"],
                                 "vol_end_date": json_file["metadata"]["vol_start_date"],
                                 },
                    "data": {}
                   }
    # 3/28 When you read this in the future, you might think the design is a
    # little weird. Remember that there were problems with the ads dataset
    # getting mutated. I'm not sure why that happened but the code below seems
    # to work. 

    for ad in json_file["data"].values():
        image = ad["image"]
        if image in complete_ads["data"]:
            complete_ads["data"][image]["for_all_campaigns"]["clicks"] += ad["clicks"] 
            complete_ads["data"][image]["for_all_campaigns"]["conversions"] += ad["conversions"] 
            complete_ads["data"][image]["for_all_campaigns"]["cost"] += ad["cost"] 
            complete_ads["data"][image]["for_all_campaigns"]["revenue"] += ad["revenue"] 
        else:
            complete_ads["data"][image] = {"for_all_campaigns": ad,
                    "for_each_campaign": []} 

    #############################
    # add the data from combined ads to "for_each_campaign" part of
    # complete_ads

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads/{date_range}_ads_dataset.json', 'r') as file:
        json_file = json.load(file)

    for ad in json_file["data"].values():
        image = ad["image"]
        complete_ads["data"][image]["for_each_campaign"].append(ad)

    
    #########################
    # fill in the rest of for_all_campaigns

    for ad_image in complete_ads["data"].values():
        clicks = ad_image["for_all_campaigns"]["clicks"]
        cost = ad_image["for_all_campaigns"]["cost"]
        revenue = ad_image["for_all_campaigns"]["revenue"]
        profit = revenue - cost
        conversions = ad_image["for_all_campaigns"]["conversions"]

        ad_image["for_all_campaigns"]["profit"] = profit
        if cost == 0:
            ad_image["for_all_campaigns"]["roi"] = 0
        else:
            ad_image["for_all_campaigns"]["roi"] = profit/cost
        if clicks == 0:
            ad_image["for_all_campaigns"]["epc"] = 0
        else:
            ad_image["for_all_campaigns"]["epc"] = profit/clicks
        if clicks == 0:
            ad_image["for_all_campaigns"]["cvr"] = 0
        else:
            ad_image["for_all_campaigns"]["cvr"] = conversions/clicks

    for ad_image in complete_ads["data"].values():
        clicks = ad_image["for_all_campaigns"]["clicks"]
        profit = ad_image["for_all_campaigns"]["profit"]
        revenue = ad_image["for_all_campaigns"]["revenue"]
        epc = ad_image["for_all_campaigns"]["epc"]
        roi = ad_image["for_all_campaigns"]["roi"]
        cvr = ad_image["for_all_campaigns"]["cvr"]
        conversions = ad_image["for_all_campaigns"]["conversions"]
        if revenue > 0:
            ad_image["for_all_campaigns"]["global_rank"] = clicks * profit * epc * roi
        else:
            if cvr == 0:
                # is this right? should it be 0?
                ad_image["for_all_campaigns"]["global_rank"] = 0
            else:
                ad_image["for_all_campaigns"]["global_rank"] = clicks * profit / cvr

    unordered_ad_images = []
    for ad_image in complete_ads["data"].values():
        unordered_ad_images.append({"ad_image": ad_image["for_all_campaigns"]["image"],
            "global_rank": ad_image["for_all_campaigns"]["global_rank"]})

    # 3/28/19 pandas isn't imported at the top of this file. Yet it still works?
    df = pd.DataFrame(unordered_ad_images)
    df = df.sort_values("global_rank", ascending=False)
    ordered_ad_images = list(df["ad_image"])

    for i in range(0, len(ordered_ad_images)):
        ad_image_name = ordered_ad_images[i]
        complete_ads["data"][ad_image_name]["for_all_campaigns"]["global_rank_order"] = i + 1

    for ad_image in complete_ads["data"].values():
        ad_image["for_all_campaigns"]["classification"] = classify_p_and_c_ads(ad_image["for_all_campaigns"]) 

    #########################
    # fill in the rest of for_each_campaign

    for ad_image in complete_ads["data"].values():
        for ad in ad_image["for_each_campaign"]:
            clicks = ad["clicks"]
            cost = ad["cost"]
            revenue = ad["revenue"]
            profit = revenue - cost
            conversions = ad["conversions"]

            ad["profit"] = profit
            if cost == 0:
                ad["roi"] = 0
            else:
                ad["roi"] = profit/cost
            if clicks == 0:
                ad["epc"] = 0
            else:
                ad["epc"] = profit/clicks
            if clicks == 0:
                ad["cvr"] = 0
            else:
                ad["cvr"] = conversions/clicks

    for ad_image in complete_ads["data"].values():
        for ad in ad_image["for_each_campaign"]:
            clicks = ad["clicks"]
            profit = ad["profit"]
            revenue = ad["revenue"]
            epc = ad["epc"]
            roi = ad["roi"]
            cvr = ad["cvr"]
            conversions = ad["conversions"]
            if revenue > 0:
                ad["rank"] = clicks * profit * epc * roi
            else:
                if cvr == 0:
                    ad["rank"] = 0
                else:
                    ad["rank"] = clicks * profit / cvr


    for ad_image in complete_ads["data"].values():
        global_rank = ad_image["for_all_campaigns"]["global_rank"]
        for ad in ad_image["for_each_campaign"]:
            rank = ad["rank"]
            ad["final_rank"] = (global_rank + rank + rank) / 3

    for ad_image in complete_ads["data"].values():
        for ad in ad_image["for_each_campaign"]:
            ad["classification"] = classify_p_and_c_ads(ad)


    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_ads/{date_range}_complete_ads_dataset.json", "w") as file:
        json.dump(complete_ads, file)



