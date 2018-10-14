from datetime import datetime, timedelta
from config.config import *
import json
import sys
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist

def create_widgets_for_one_campaign_dataset(mgid_token, vol_token,
        mgid_campaign_id, vol_campaign_id, start_date, end_date, output_name):
    # create a special mgid_end_date because it needs to be one day earlier than 
    # the voluum date in order for the data from both requests to have the same
    # dates
    mgid_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    mgid_end_date = (mgid_end_date - timedelta(1)).strftime("%Y-%m-%d")

    # get clicks and costs for each widget from mgid
    mgid_widget_data = get_mgid_widget_clicks_and_costs_by_campaign(mgid_token,
            mgid_campaign_id, start_date,
            mgid_end_date)

    # get conversion data for each widget from voluum
    vol_results = get_vol_widget_conversions_by_campaign(vol_token,
            vol_campaign_id, start_date,
            end_date)
    
    excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            mgid_campaign_id)

    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    # merge the data from mgid and voluum into one dictionary
    for widget_id in mgid_widget_data:
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

        if widget_id in widget_whitelist:
            mgid_widget_data[widget_id]['global_status'] = "whitelist" 
        elif widget_id in widget_greylist:
            mgid_widget_data[widget_id]['global_status'] = "greylist" 
        elif widget_id in widget_blacklist:
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

