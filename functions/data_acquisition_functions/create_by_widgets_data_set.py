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

def create_by_widgets_data_set(widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = {}

    for campaign in campaigns:
        with open(f'/home/bsh/Documents/UlanMedia/data/by_campaigns_by_widgets_data/{campaign["vol_id"]}_{date_range}_by_campaigns_by_widgets_data.json', 'r') as file:
             data = json.load(file)

        if widget_id not in data.keys():
            continue
        else:
            widget_data[campaign["vol_id"]] = data[widget_id]
            widget_data[campaign["vol_id"]]["vol_id"] = campaign["vol_id"]
            widget_data[campaign["vol_id"]]["mgid_id"] = campaign["mgid_id"]
            widget_data[campaign["vol_id"]]["name"] = campaign["name"]
            
    complete_widget_data = widget_data 

    with open(f"../../data/by_widgets_data/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")
