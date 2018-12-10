from datetime import datetime, timedelta
from config.config import *
import json
import sys
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist

def create_campaigns_for_one_p_widget_dataset(parent_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = {"metadata": {"mgid_start_date": "",
                               "mgid_end_date": "",
                               "vol_start_date": "",
                               "vol_end_date": ""
                               },
                    "data": []
                  } 

    for campaign in campaigns:
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{campaign["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
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
        
        parent_widget_data = {}
        for widget_id in widget_ids_with_matching_parent:
            if not parent_widget_data:
                parent_widget_data = {
                "widget_id": parent_widget_id, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "max_lead_cpa": campaign["max_lead_cpa"],
                "max_sale_cpa": campaign["max_sale_cpa"],
                "status": data[widget_id]["status"],
                "global_status": data[widget_id]["global_status"],
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
            widget_data["data"].append(parent_widget_data)
            
    complete_widget_data = widget_data 

    with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    return json.dumps(complete_widget_data)

