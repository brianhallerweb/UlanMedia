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

def create_by_parent_widgets_data_set(parent_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = [] 

    for campaign in campaigns:
        with open(f'/home/bsh/Documents/UlanMedia/data/by_campaigns_by_widgets_data/{campaign["vol_id"]}_{date_range}_by_campaigns_by_widgets_data.json', 'r') as file:
             data = json.load(file)

        widget_ids_with_matching_parent = []
        for widget_id in list(data.keys()):
            if widget_id.startswith(parent_widget_id):
                widget_ids_with_matching_parent.append(widget_id)

        for widget_id in widget_ids_with_matching_parent:
            temp = data[widget_id] 
            temp["vol_id"] = campaign["vol_id"]
            temp["mgid_id"] = campaign["mgid_id"]
            temp["name"] = campaign["name"]
            widget_data.append(temp)
            
    complete_widget_data = widget_data 

    with open(f"../../data/by_parent_widgets_data/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")

