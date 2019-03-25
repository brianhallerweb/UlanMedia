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


def combine_mgid_vol_ads_data(mgid_token, vol_token, date_range,vol_start_date,
        vol_end_date, mgid_data, vol_data):
    # This function will combine the mgid ads data and the vol ads data. Both
    # data sets are dictionaries with keys = ad id and values = dictionaries of
    # data for that ad id. 

    # create a look up dictionary so you can find vol id, and campaign name from mgid id
    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["mgid_id"]] = [campaign["vol_id"],
        campaign["name"]]
    
    # combining mgid and vol by ad_id
    combined_ads = {"metadata": {"vol_start_date": vol_start_date,
                                 "vol_end_date": vol_end_date
                                 },
                    "data": {}
                   }

    for ad in mgid_data.values():
        ad_id = ad["ad_id"]  
        mgid_id = ad["mgid_id"]
        if mgid_id not in campaigns_lookup:
            continue
        vol_id = campaigns_lookup[mgid_id][0]
        name = campaigns_lookup[mgid_id][1]
        if ad_id in vol_data:
            vol_ad_data = vol_data[ad_id]
            ad["vol_id"] = vol_id
            ad["name"] = name
            ad["clicks"] = vol_ad_data["clicks"]
            ad["cost"] = vol_ad_data["cost"]
            ad["conversions"] = vol_ad_data["conversions"]
            ad["revenue"] = vol_ad_data["revenue"]
        else:
            ad["vol_id"] = vol_id
            ad["name"] = name
            ad["clicks"] = 0
            ad["cost"] = 0
            ad["conversions"] = 0
            ad["revenue"] = 0 
        combined_ads["data"][ad_id] = ad 
    
    ##############################
    # start of the creation of complete_ads

    complete_ads = {"metadata": {"vol_start_date": vol_start_date,
                                 "vol_end_date": vol_end_date
                                 },
                    "data": {}
                   }

    ############################
    # add the "for_all_campaigns" part

    for ad in combined_ads["data"].values():
        image = ad["image"]
        if image in complete_ads["data"]:
            complete_ads["data"][image]["for_all_campaigns"]["clicks"] += ad["clicks"] 
            complete_ads["data"][image]["for_all_campaigns"]["conversions"] += ad["conversions"] 
            complete_ads["data"][image]["for_all_campaigns"]["cost"] += ad["cost"] 
            complete_ads["data"][image]["for_all_campaigns"]["revenue"] += ad["revenue"] 
        else:
            complete_ads["data"][image] = {"for_all_campaigns": ad,
                    "for_each_campaign": []}

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

    #############################
    # add the "for_each_campaign" part

    for ad in combined_ads["data"].values():
        image = ad["image"]
        complete_ads["data"][image]["for_each_campaign"].append(ad)

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


    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/ads/{date_range}_ads_dataset.json", "w") as file:
        json.dump(complete_ads, file)



