from config.config import *
import json
import sys
from functions.misc.get_campaign_sets import get_campaign_sets

def create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, output_name):
    campaigns = get_campaign_sets()

    campaigns_for_one_c_widget = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": [] 
                                } 

    for campaign in campaigns:
        vol_id = campaign["vol_id"]
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             json_file = json.load(file)
        
        metadata = json_file["metadata"]
        data = json_file["data"]

        # add metadata
        if not campaigns_for_one_c_widget["metadata"]["mgid_start_date"]:
             campaigns_for_one_c_widget["metadata"]["mgid_start_date"] = metadata["mgid_start_date"]
        if not campaigns_for_one_c_widget["metadata"]["mgid_end_date"]:
             campaigns_for_one_c_widget["metadata"]["mgid_end_date"] = metadata["mgid_end_date"]
        if not campaigns_for_one_c_widget["metadata"]["vol_start_date"]:
             campaigns_for_one_c_widget["metadata"]["vol_start_date"] = metadata["vol_start_date"]
        if not campaigns_for_one_c_widget["metadata"]["vol_end_date"]:
             campaigns_for_one_c_widget["metadata"]["vol_end_date"] = metadata["vol_end_date"]

        c_widget_data = {}
        for widget in data:
            if widget == c_widget_id:
                c_widget_data = {
                "widget_id": widget, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "max_lead_cpa": campaign["max_lead_cpa"],
                "max_sale_cpa": campaign["max_sale_cpa"],
                "status": data[widget]["status"],
                "global_status": data[widget]["global_status"],
                "clicks": data[widget]["clicks"], 
                "cost": data[widget]["cost"],
                "sales": data[widget]["sales"],
                "leads": data[widget]["leads"],
                "revenue": data[widget]["revenue"],
                }

        if c_widget_data:
            campaigns_for_one_c_widget["data"].append(c_widget_data)
            
    complete_widget_data = campaigns_for_one_c_widget 

    with open(f"../../data/campaigns_for_one_c_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    return json.dumps(complete_widget_data)


