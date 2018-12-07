from config.config import *
import json
import sys
from functions.misc.get_campaign_sets import get_campaign_sets

def create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    widget_data = [] 

    for campaign in campaigns:
        vol_id = campaign["vol_id"]
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             data = json.load(file)

        c_widget_data = {}
        for widget in data:
            if widget == c_widget_id:
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


