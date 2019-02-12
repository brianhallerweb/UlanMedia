from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
import json
import os
import sys

def create_campaigns_for_one_offer_dataset(date_range, offer_id):
    # The goal of this function is to return a json dataset for
    # campaigns_for_one_offer. That means each row is a campaign and each
    # column is data for one offer. 
    #
    # The resulting data structure looks like this:
    # {"metadata": {"mgid_start_date": "2018-08-09",
    #               "mgid_end_date": "2019-02-04",
    #               "vol_start_date": "2018-08-09",
    #               "vol_end_date": "2019-02-05"},
    #  "data": [{"clicks": 113,
    #            "cost": 6.82821,
    #            "offerID": "61bd8d29-7f6d-49cd-a70f-aa81d8f6db7a",
    #            "campaignID": "9904c4e6-63de-4f19-8947-641e81a488fd",
    #            "profit": -6.82821,
    #            "conversions": 1,
    #            "campaignName": "bin_europe-t1_english_desktop_cpc_0.06",
    #            "offerName": "Pattern Trader NL",
    #            "offerFlow": "(bin: ctGeo - Dutch)"}
    #            {...},
    #           .
    #           .
    #           .
    #           }
    # }
    ########################################################

    # 1. Get some prerequisite data.
    
    # Create a lookup dictionary so that you can find the campaign name from the vol_id
    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["name"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers/{date_range}_offers_dataset.json', 'r') as file:
        json_file = json.load(file)

    # the offers dataset looks like this:
    # {data: campaignId: {offerid: {offer data}}}

    #{"metadata": {"vol_start_date": "2018-11-13", "vol_end_date": "2019-02-11"},
    # "data": {"85446ad7-7b2d-45c1-a3c5-dbe8b3d2a443": {"7ae5f17e-563b-4f06-9fb5-836c5c662a9a": {"clicks": 4,
    #                                                                                            "cost": 0.11416,
    #                                                                                            "offerID":"7ae5f17e-563b-4f06-9fb5-836c5c662a9a",
    #                                                                                            "campaignID": "85446ad7-7b2d-45c1-a3c5-dbe8b3d2a443",
    #                                                                                            "profit": -0.11416,
    #                                                                                            "conversions": 0,
    #                                                                                            "campaignName": "bin_world-wide-t1_spanish_mobile_cpc_0.045",
    #                                                                                            "offerName": "404",
    #                                                                                            "offerFlow": "404"}

    metadata = json_file["metadata"]
    data = json_file["data"]

    #####################################################

    # 2. set up the basic data structure you want to create

    campaigns_for_one_offer = {"metadata": metadata, "data": []}   

    ########################################################

    # 3. loop through the offers data to create campaigns_for_one_offer

    for campaign in data:
        for offer in data[campaign]:
            if offer == offer_id:
                campaigns_for_one_offer["data"].append(data[campaign][offer])

    for campaign in campaigns_for_one_offer["data"]:
        name = campaigns_lookup[campaign["campaignID"]]
        campaign["campaignName"] = name

    ########################################################

    # 3. Save p_widgets_for_all_campaigns to a json file and return it as a
    # json file 

    with open(f"../../data/campaigns_for_one_offer/{offer_id}_{date_range}_campaigns_for_one_offer_dataset.json", "w") as file:
        json.dump(campaigns_for_one_offer, file)
    
    return json.dumps(campaigns_for_one_offer)

