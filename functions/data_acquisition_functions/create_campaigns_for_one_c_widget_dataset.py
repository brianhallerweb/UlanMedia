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

def create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = [] 

    for campaign in campaigns:
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{campaign["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             data = json.load(file)

       # I am here, why can't a match a c widget id with a widget in any of the
       # p and c widgets for one campaigns. If the c widget exists, it must be
       # in some campaign. That c widget ultimately came from p and c widgets
       # for one campaign. Here I am looping through all the p and c widgets
       # for one campaigns, so I should be able to find it. My data is a day or
       # so old so maybe that is the problem? Start by updating your data. 
        c_widget_data = {}
        for widget in data.keys():

            if widget == c_widget_id:
                print("here")
                c_widget_data = {
                "widget_id": widget, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "max_lead_cpa": data[widget]["max_lead_cpa"],
                "max_sale_cpa": data[widget]["max_sale_cpa"],
                "status": data[widget]["status"],
                "global_status": data[widget]["global_status"],
                "clicks": data[widget]["clicks"], 
                "cost": data[widget]["cost"],
                "sales": data[widget]["sales"],
                "leads": data[widget]["leads"],
                "revenue": data[widget]["revenue"],
                }

        if c_widget_data:
            widget_data.append(c_widget_data)
            
    complete_widget_data = widget_data 

    with open(f"../../data/campaigns_for_one_c_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)


