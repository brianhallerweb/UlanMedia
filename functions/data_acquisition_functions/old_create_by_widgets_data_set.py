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

def create_by_widgets_data_set(mgid_token, vol_token, widget_id, start_date, end_date, output_name):
    # create a special mgid_end_date because it needs to be one day earlier than 
    # the voluum date in order for the data from both requests to have the same
    # dates
    mgid_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    mgid_end_date = (mgid_end_date - timedelta(1)).strftime("%Y-%m-%d")

    # get widget list (white, grey, black)
    # The lists are curated by mike to keep track of widgets that have been
    # historically good or bad.
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    # get campaigns in campaign_sets.txt
    campaigns = get_campaign_sets()
    
    # widgets_data dictionary is the output of this function
    # the key is vol_id 
    # the value is widget data (there is only one widget per dictionary)
    widget_data = {}
    for campaign in campaigns:
        # get clicks and costs for each widget from mgid
        # you are reusing this function from by_campaigns_by_widgets
        mgid_widget_data = get_mgid_widget_clicks_and_costs_by_campaign(mgid_token,
                str(campaign["mgid_id"]), start_date,
                mgid_end_date)
        print("mgid widget data acquired")
        # check if the widget even exists for that campaign
        # if not, just go to the next campaign
        if widget_id not in mgid_widget_data:
            continue
        else:
            widget_data[campaign["vol_id"]] = mgid_widget_data[widget_id]
            widget_data[campaign["vol_id"]]["vol_id"] = campaign["vol_id"]
            widget_data[campaign["vol_id"]]["mgid_id"] = campaign["mgid_id"]
            widget_data[campaign["vol_id"]]["name"] = campaign["name"]
            
        # get conversion data for each widget from voluum
        # you are reusing this function from by_campaigns_by_widgets
        vol_results = get_vol_widget_conversions_by_campaign(vol_token,
                campaign["vol_id"], start_date,
                end_date)
        print("vol widget data acquired")
        # add the widget data from voluum to widgets_data
        if widget_id not in vol_results:
            widget_data[campaign["vol_id"]]['revenue'] = 0.0 
            widget_data[campaign["vol_id"]]['leads'] = 0 
            widget_data[campaign["vol_id"]]['sales'] = 0.0 
            widget_data[campaign["vol_id"]]['referrer'] = [] 
        else:
            vol_widget = vol_results[widget_id]
            for key in vol_widget:
                widget_data[campaign["vol_id"]][key] = vol_widget[key]

        # check if widget has been excluded before
        excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            str(campaign["mgid_id"]))
        if widget_id not in excluded_widgets:
            widget_data[campaign["vol_id"]]['status'] = "included" 
        else:
            widget_data[campaign["vol_id"]]['status'] = "excluded" 

        if widget_id in widget_whitelist:
            widget_data[campaign["vol_id"]]['global_status'] = "whitelist" 
        elif widget_id in widget_greylist:
            widget_data[campaign["vol_id"]]['global_status'] = "greylist" 
        elif widget_id in widget_blacklist:
            widget_data[campaign["vol_id"]]['global_status'] = "blacklist" 
        else:
            widget_data[campaign["vol_id"]]['global_status'] = "not yet listed" 

    print("widget data for all campaigns collected and aggregagted")


    complete_widget_data = []
    for widget in widget_data.values():
        complete_widget_data.append(widget)

    with open(f"../../data/by_widgets_data/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")

