from config.config import *
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.create_mgid_date_range import create_mgid_date_range
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from datetime import datetime, timedelta
import json
import sys
import re

def create_p_and_c_widgets_for_one_campaign_dataset(mgid_token, vol_token,
        campaign, days_ago, output_name):
    # create mgid and vol dates
    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    mgid_dates = create_mgid_date_range(days_ago, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]

    # extract needed campaign info from mgid and vol
    mgid_id = campaign["mgid_id"]
    vol_id = campaign["vol_id"]
    max_lead_cpa = campaign["max_lead_cpa"] 
    max_sale_cpa = campaign["max_sale_cpa"] 

    # create a metadata dictionary
    metadata = {"mgid_start_date": mgid_start_date,
            "mgid_end_date": mgid_end_date,
            "vol_start_date": vol_start_date,
            "vol_end_date": vol_end_date,
            "mgid_id": campaign["mgid_id"],
            "vol_id": campaign["vol_id"],
            "max_lead_cpa": campaign["max_lead_cpa"],
            "max_sale_cpa": campaign["max_sale_cpa"] 
             }

    # get clicks and costs for each widget from mgid
    mgid_widget_data = get_mgid_widget_clicks_and_costs_by_campaign(mgid_token,
            mgid_id, mgid_start_date,
            mgid_end_date)

    # get conversion data for each widget from vol
    vol_results = get_vol_widget_conversions_by_campaign(vol_token,
            vol_id, vol_start_date,
            vol_end_date)
    
    # excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            # mgid_id)

    # regex for extracting parent widget id
    # pattern = re.compile(r'\d*')

    # merge the data from mgid and voluum into one dictionary
    for widget_id in mgid_widget_data:

        if widget_id not in vol_results:
            mgid_widget_data[widget_id]['revenue'] = 0.0 
            mgid_widget_data[widget_id]['leads'] = 0 
            mgid_widget_data[widget_id]['sales'] = 0 
            mgid_widget_data[widget_id]['referrer'] = [] 
        else:
            vol_widget = vol_results[widget_id]
            for key in vol_widget:
                mgid_widget_data[widget_id][key] = vol_widget[key]

        # 1/1/19 - I removed the status and global status data acquisition from
        # this script because it needs to be updated upon "submit" on the
        # dashboard. When using the dashboard, we often change the status and
        # global status of widgets and we want that to be reflected
        # immediately - or at least on the next "submit"

        # This regex on widget_id extracts the parent widget_id
        # The reason for this extraction is that the white grey black
        # lists, and excluded_list only include parent widget ids.
        # if pattern.search(widget_id).group() not in excluded_widgets:
            # mgid_widget_data[widget_id]['status'] = "included" 
        # else:
            # mgid_widget_data[widget_id]['status'] = "excluded" 


    complete_widget_data = mgid_widget_data

    complete_data_ready_for_json = {"metadata": metadata,
            "data": complete_widget_data}

    with open(f"../../data/p_and_c_widgets_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(complete_data_ready_for_json, file)

    print(f"{output_name} created")

