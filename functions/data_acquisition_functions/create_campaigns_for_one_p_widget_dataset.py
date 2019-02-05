from config.config import *
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.classification_functions.classify_campaign_for_one_p_widget import classify_campaign_for_one_p_widget
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from datetime import datetime, timedelta
import json
import os
import sys
import re

def create_campaigns_for_one_p_widget_dataset(parent_widget_id, date_range, output_name):
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()


    parent_widget_global_status = ""
    if parent_widget_id in widget_whitelist:
       parent_widget_global_status = "whitelist" 
    elif parent_widget_id in widget_greylist:
       parent_widget_global_status = "greylist" 
    elif parent_widget_id in widget_blacklist:
       parent_widget_global_status = "blacklist" 
    else:
       parent_widget_global_status = "not yet listed" 

    campaigns = get_campaign_sets()

    widget_data = {"metadata": {"mgid_start_date": "",
                               "mgid_end_date": "",
                               "vol_start_date": "",
                               "vol_end_date": ""
                               },
                    "data": []
                  } 

    for campaign in campaigns:
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaign["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             json_file = json.load(file)

        metadata = json_file["metadata"]
        data = json_file["data"]
        

        # add metadata
        if not widget_data["metadata"]["mgid_start_date"]:
             widget_data["metadata"]["mgid_start_date"] = metadata["mgid_start_date"]
        if not widget_data["metadata"]["mgid_end_date"]:
             widget_data["metadata"]["mgid_end_date"] = metadata["mgid_end_date"]
        if not widget_data["metadata"]["vol_start_date"]:
             widget_data["metadata"]["vol_start_date"] = metadata["vol_start_date"]
        if not widget_data["metadata"]["vol_end_date"]:
             widget_data["metadata"]["vol_end_date"] = metadata["vol_end_date"]

        # add widget data
        widget_ids_with_matching_parent = []
        for widget_id in list(data.keys()):
            if widget_id.startswith(parent_widget_id):
                widget_ids_with_matching_parent.append(widget_id)

        # 1/24/19 This is for updating the campaign status on each submit
        # press on campaigns_for_one_p_widget
        # get list of excluded widgets
        with open(f'{os.environ.get("ULANMEDIAAPP")}/excluded_p_widgets_lists/{campaign["mgid_id"]}_excluded_p_widgets.json', 'r') as file:
             excluded_widgets = json.load(file)
        # regex for extracting parent widget id
        pattern = re.compile(r'\d*')

        parent_widget_data = {}
        for widget_id in widget_ids_with_matching_parent:
            if pattern.search(widget_id).group() not in excluded_widgets:
                widget_status = "included" 
            else:
                widget_status = "excluded" 

            if not parent_widget_data:
                parent_widget_data = {
                "widget_id": parent_widget_id, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "max_lead_cpa": campaign["max_lead_cpa"],
                "max_sale_cpa": campaign["max_sale_cpa"],
                "status": widget_status,
                "global_status": parent_widget_global_status,
                "clicks": data[widget_id]["clicks"], 
                "cost": data[widget_id]["cost"],
                "sales": data[widget_id]["sales"],
                "leads": data[widget_id]["leads"],
                "revenue": data[widget_id]["revenue"],
                }
            else:
                parent_widget_data["clicks"] += data[widget_id]["clicks"]
                parent_widget_data["cost"] += data[widget_id]["cost"]
                parent_widget_data["sales"] += data[widget_id]["sales"]
                parent_widget_data["leads"] += data[widget_id]["leads"]
                parent_widget_data["revenue"] += data[widget_id]["revenue"]

        if parent_widget_data:
            # this is where each campaign is classified as good, half good,
            # bad, half bad, wait
            parent_widget_data["classification"] = classify_campaign_for_one_p_widget(parent_widget_data)
            widget_data["data"].append(parent_widget_data)
            
    complete_widget_data = widget_data 

    with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    return json.dumps(complete_widget_data)

