from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
import json
import os
import sys
import re

def create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range,
        output_name):
    ########################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)
    
    complete_p_widget = complete_p_widgets[p_widget_id]

    ########################################################

    # 2. set up the basic data structure you want to create

    campaigns_for_one_p_widget = {"metadata":{}, "data":[]} 

    #########################################################

    # 3. Add the metadata. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    campaigns_for_one_p_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    campaigns_for_one_p_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    campaigns_for_one_p_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    campaigns_for_one_p_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]
    campaigns_for_one_p_widget["metadata"]["p_widget_classification"] = complete_p_widget["for_all_campaigns"]["classification"]
    campaigns_for_one_p_widget["metadata"]["good_campaigns_count"] = complete_p_widget["good_campaigns_count"]
    campaigns_for_one_p_widget["metadata"]["bad_campaigns_count"] = complete_p_widget["bad_campaigns_count"]
    campaigns_for_one_p_widget["metadata"]["wait_campaigns_count"] = complete_p_widget["wait_campaigns_count"]

    #########################################################

    # 4. Add the data

    campaigns_for_one_p_widget["data"] = complete_p_widget["for_each_campaign"]

    ############################################################
    # 11. Save campaigns_for_one_p_widget to a json file and return it as a
    # json file 

    with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        json.dump(campaigns_for_one_p_widget, file)

    return json.dumps(campaigns_for_one_p_widget)

