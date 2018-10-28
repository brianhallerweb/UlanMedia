from datetime import datetime, timedelta
from config.config import *
import json
import sys
import re
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.create_mgid_date_range import create_mgid_date_range


def create_widgets_for_one_campaign_dataset(mgid_token, vol_token,
        campaign, days_ago, output_name):
    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    mgid_dates = create_mgid_date_range(days_ago, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]
    print(f"vol start date: {vol_start_date}")
    print(f"vol end date: {vol_end_date}")
    print(f"mgid start date: {mgid_start_date}")
    print(f"mgid end date: {mgid_end_date}")

    # extract needed campaign info
    mgid_campaign_id = str(campaign["mgid_id"])
    vol_campaign_id = campaign["vol_id"]
    max_lead_cpa = campaign["max_lead_cpa"] 
    max_sale_cpa = campaign["max_sale_cpa"] 


    # get clicks and costs for each widget from mgid
    mgid_widget_data = get_mgid_widget_clicks_and_costs_by_campaign(mgid_token,
            mgid_campaign_id, mgid_start_date,
            mgid_end_date)

    # get conversion data for each widget from voluum
    vol_results = get_vol_widget_conversions_by_campaign(vol_token,
            vol_campaign_id, vol_start_date,
            vol_end_date)
    
    excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            mgid_campaign_id)

    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()
    pattern = re.compile(r'\d*')

    # merge the data from mgid and voluum into one dictionary
    for widget_id in mgid_widget_data:
        # add max_lead_cpa and max_sale_cpa to each widget
        # this is used in the data_analysis script for filtering
        # purposes
        mgid_widget_data[widget_id]['max_lead_cpa'] = max_lead_cpa 
        mgid_widget_data[widget_id]['max_sale_cpa'] = max_sale_cpa 

        if widget_id not in vol_results:
            mgid_widget_data[widget_id]['revenue'] = 0.0 
            mgid_widget_data[widget_id]['leads'] = 0 
            mgid_widget_data[widget_id]['sales'] = 0.0 
            mgid_widget_data[widget_id]['referrer'] = [] 
        else:
            vol_widget = vol_results[widget_id]
            for key in vol_widget:
                mgid_widget_data[widget_id][key] = vol_widget[key]

        if widget_id not in excluded_widgets:
            mgid_widget_data[widget_id]['status'] = "included" 
        else:
            mgid_widget_data[widget_id]['status'] = "excluded" 

        # This regex on widget_id extracts the parent widget_id
        # The reason for this extraction is that the white grey black
        # lists only include parent widget ids.
        if pattern.search(widget_id).group() in widget_whitelist:
            mgid_widget_data[widget_id]['global_status'] = "whitelist" 
        elif pattern.search(widget_id).group() in widget_greylist:
            mgid_widget_data[widget_id]['global_status'] = "greylist" 
        elif pattern.search(widget_id).group() in widget_blacklist:
            mgid_widget_data[widget_id]['global_status'] = "blacklist" 
        else:
            mgid_widget_data[widget_id]['global_status'] = "not yet listed" 

 

    complete_widget_data = mgid_widget_data
    #complete_widget_data = []
    #for widget in mgid_widget_data.values():
    #    complete_widget_data.append(widget)

    with open(f"../../data/widgets_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")
