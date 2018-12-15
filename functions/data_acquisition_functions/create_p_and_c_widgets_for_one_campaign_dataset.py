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
    
    excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            mgid_id)

    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    # regex for extracting parent widget id
    pattern = re.compile(r'\d*')

    # merge the data from mgid and voluum into one dictionary
    for widget_id in mgid_widget_data:

        if widget_id not in vol_results:
            mgid_widget_data[widget_id]['revenue'] = 0.0 
            mgid_widget_data[widget_id]['leads'] = 0 
            # 12/7/18 why is sales 0.0 and not just 0
            mgid_widget_data[widget_id]['sales'] = 0.0 
            mgid_widget_data[widget_id]['referrer'] = [] 
        else:
            vol_widget = vol_results[widget_id]
            for key in vol_widget:
                mgid_widget_data[widget_id][key] = vol_widget[key]

        # This regex on widget_id extracts the parent widget_id
        # The reason for this extraction is that the white grey black
        # lists, and excluded_list only include parent widget ids.
        if pattern.search(widget_id).group() not in excluded_widgets:
            mgid_widget_data[widget_id]['status'] = "included" 
        else:
            mgid_widget_data[widget_id]['status'] = "excluded" 

        if pattern.search(widget_id).group() in widget_whitelist:
            mgid_widget_data[widget_id]['global_status'] = "whitelist" 
        elif pattern.search(widget_id).group() in widget_greylist:
            mgid_widget_data[widget_id]['global_status'] = "greylist" 
        elif pattern.search(widget_id).group() in widget_blacklist:
            mgid_widget_data[widget_id]['global_status'] = "blacklist" 
        else:
            mgid_widget_data[widget_id]['global_status'] = "not yet listed" 

    complete_widget_data = mgid_widget_data

    complete_data_ready_for_json = {"metadata": metadata,
            "data": complete_widget_data}

    with open(f"../../data/p_and_c_widgets_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(complete_data_ready_for_json, file)

    print(f"{output_name} created")

