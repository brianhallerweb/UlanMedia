from config.config import *
from config.mgid_token import mgid_token
import os
import json

def create_p_widgets_for_one_campaign_dataset(mgid_token, vol_id, date_range):

    p_widgets_for_one_campaign = {"metadata": {},
                                 "data": [] 
                                } 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    p_widgets_for_one_campaign["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    p_widgets_for_one_campaign["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    p_widgets_for_one_campaign["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    p_widgets_for_one_campaign["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for p_widget in data:
        for campaign in data[p_widget]["for_each_campaign"]:
            if campaign["vol_id"] == vol_id:
                campaign["classification"] = data[p_widget]["for_all_campaigns"]["classification"]
                campaign["global_status"] = data[p_widget]["for_all_campaigns"]["global_status"]
                p_widgets_for_one_campaign["data"].append(campaign)

    with open(f"../../data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)

    return json.dumps(p_widgets_for_one_campaign)
