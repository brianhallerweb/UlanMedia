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

def create_complete_ads_dataset(date_range, combined_ads):

    complete_ads = {"metadata": {"vol_start_date": combined_ads["metadata"]["vol_start_date"],
                                 "vol_end_date": combined_ads["metadata"]["vol_start_date"],
                                 },
                    "data": {}
                   }

    # The code in this first part is a little strange. I tried to use
    # combined_ads to populate the for_all_campaigns and the for_each_campaign
    # part of complete_ads but the process was mutating combined ads.

    #############################
    # add the data from combined ads to "for_each_campaign" part of
    # complete_ads

    for ad in combined_ads["data"].values():
        image = ad["image"]
        complete_ads["data"][image] = {"for_all_campaigns": {}, "for_each_campaign": []}
        complete_ads["data"][image]["for_each_campaign"].append(ad)

    ############################
    # add the data from combined ads to "for_all_campaigns" part of
    # complete_ads

    for ad in combined_ads["data"].values():
        image = ad["image"]
        if complete_ads["data"][image]["for_all_campaigns"]:
            complete_ads["data"][image]["for_all_campaigns"]["clicks"] += ad["clicks"] 
            complete_ads["data"][image]["for_all_campaigns"]["conversions"] += ad["conversions"] 
            complete_ads["data"][image]["for_all_campaigns"]["cost"] += ad["cost"] 
            complete_ads["data"][image]["for_all_campaigns"]["revenue"] += ad["revenue"] 
        else:
            complete_ads["data"][image]["for_all_campaigns"] = ad 

    # for ad_image in combined_ads["data"].values():
        # pp.pprint(ad_image)
        # if ad_image.get("bullshit"):
            # print("here")
            # sys.exit()
    # sys.exit()

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
                ad_image["for_all_campaigns"]["global_rank"] = 0
            else:
                ad_image["for_all_campaigns"]["global_rank"] = clicks * profit / cvr


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

    pp.pprint(complete_ads)
    sys.exit()


    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/ads/{date_range}_ads_dataset.json", "w") as file:
        json.dump(complete_ads, file)



