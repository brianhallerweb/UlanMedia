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

def create_campaigns_for_one_total_widget_dataset(total_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = [] 

    for campaign in campaigns:
        with open(f'/home/bsh/Documents/UlanMedia/data/widgets_for_one_campaign/{campaign["vol_id"]}_{date_range}_widgets_for_one_campaign_dataset.json', 'r') as file:
             data = json.load(file)

        for widget_id in list(data.keys()):
            if widget_id == total_widget_id:
                temp = data[widget_id] 
                temp["vol_id"] = campaign["vol_id"]
                temp["mgid_id"] = campaign["mgid_id"]
                temp["name"] = campaign["name"]
                widget_data.append(temp)
            
    complete_widget_data = widget_data 

    with open(f"../../data/campaigns_for_one_total_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")

