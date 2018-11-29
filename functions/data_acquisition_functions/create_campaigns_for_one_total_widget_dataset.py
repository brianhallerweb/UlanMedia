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

        widget_ids_with_matching_total = []
        for widget_id in list(data.keys()):
            if widget_id.startswith(total_widget_id):
                widget_ids_with_matching_total.append(widget_id)

        total_widget_data = {}
        for widget_id in widget_ids_with_matching_total:
            if not total_widget_data:
                total_widget_data = {
                "widget_id": total_widget_id, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "max_lead_cpa": data[widget_id]["max_lead_cpa"],
                "max_sale_cpa": data[widget_id]["max_sale_cpa"],
                "status": data[widget_id]["status"],
                "global_status": data[widget_id]["global_status"],
                "clicks": data[widget_id]["clicks"], 
                "cost": data[widget_id]["cost"],
                "sales": data[widget_id]["sales"],
                "leads": data[widget_id]["leads"],
                "revenue": data[widget_id]["revenue"],
                }
            else:
                total_widget_data["clicks"] += data[widget_id]["clicks"]
                total_widget_data["cost"] += data[widget_id]["cost"]
                total_widget_data["sales"] += data[widget_id]["sales"]
                total_widget_data["leads"] += data[widget_id]["leads"]
                total_widget_data["revenue"] += data[widget_id]["revenue"]

        if total_widget_data:
            widget_data.append(total_widget_data)
            
    complete_widget_data = widget_data 

    with open(f"../../data/campaigns_for_one_total_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    print(f"{output_name} created")

