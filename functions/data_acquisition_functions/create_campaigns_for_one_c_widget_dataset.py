from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
import os
import json
import sys
import re

def create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range,
        output_name):

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_c_widgets/{date_range}_complete_c_widgets_dataset.json', 'r') as file:
        complete_c_widgets = json.load(file)
    
    complete_c_widget = complete_c_widgets[c_widget_id]

    ########################################################

    # 2. set up the basic data structure you want to create

    campaigns_for_one_c_widget = {"metadata":{}, "data":[]} 

    #########################################################

    # 3. Add the metadata. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    campaigns_for_one_c_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    campaigns_for_one_c_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    campaigns_for_one_c_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    campaigns_for_one_c_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]
    campaigns_for_one_c_widget["metadata"]["c_widget_classification"] = complete_c_widget["for_all_campaigns"]["classification"]
    campaigns_for_one_c_widget["metadata"]["c_widget_global_status"] = complete_c_widget["for_all_campaigns"]["global_status"]
    campaigns_for_one_c_widget["metadata"]["c_widget_has_mismatch_classification_and_global_status"] = complete_c_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"]
    campaigns_for_one_c_widget["metadata"]["good_campaigns_count"] = complete_c_widget["good_campaigns_count"]
    campaigns_for_one_c_widget["metadata"]["bad_campaigns_count"] = complete_c_widget["bad_campaigns_count"]
    campaigns_for_one_c_widget["metadata"]["not_yet_campaigns_count"] = complete_c_widget["not_yet_campaigns_count"]

    #########################################################

    # 4. Add the data

    campaigns_for_one_c_widget["data"] = complete_c_widget["for_each_campaign"]

    ############################################################
    # 5. Save campaigns_for_one_c_widget to a json file and return it as a
    # json file 

    with open(f"../../data/campaigns_for_one_c_widget/{output_name}.json", "w") as file:
        json.dump(campaigns_for_one_c_widget, file)

    return json.dumps(campaigns_for_one_c_widget)
