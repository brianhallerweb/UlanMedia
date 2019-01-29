import json
from config.config import *
import re
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
import os

def create_p_widgets_for_one_campaign_dataset(mgid_token, vol_id, date_range):
    campaigns = get_campaign_sets()
    mgid_id = ""
    for campaign in campaigns:
        if campaign["vol_id"] == vol_id:
            mgid_id = campaign["mgid_id"]

    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, mgid_id)

    p_widgets_for_one_campaign = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}
                                } 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
       json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]
    
    p_widgets_for_one_campaign["metadata"] = metadata

    pattern = re.compile(r'\d*')
    for widget in data:
       parent_widget = pattern.search(widget).group()
       if parent_widget in p_widgets_for_one_campaign["data"]:
           p_widgets_for_one_campaign["data"][parent_widget]["clicks"] += data[widget]["clicks"]
           p_widgets_for_one_campaign["data"][parent_widget]["cost"] += data[widget]["cost"]
           p_widgets_for_one_campaign["data"][parent_widget]["revenue"] += data[widget]["revenue"]
           p_widgets_for_one_campaign["data"][parent_widget]["leads"] += data[widget]["leads"]
           p_widgets_for_one_campaign["data"][parent_widget]["sales"] += data[widget]["sales"]
       else:
           p_widgets_for_one_campaign["data"][parent_widget] = data[widget]
           p_widgets_for_one_campaign["data"][parent_widget]["widget_id"] = parent_widget

           if parent_widget in excluded_widgets:
               p_widgets_for_one_campaign["data"][parent_widget]['status'] = "excluded" 
           else:
               p_widgets_for_one_campaign["data"][parent_widget]['status'] = "included" 

           if parent_widget in widget_whitelist:
               p_widgets_for_one_campaign["data"][parent_widget]['global_status'] = "whitelist" 
           elif parent_widget in widget_greylist:
               p_widgets_for_one_campaign["data"][parent_widget]['global_status'] = "greylist" 
           elif parent_widget in widget_blacklist:
               p_widgets_for_one_campaign["data"][parent_widget]['global_status'] = "blacklist" 
           else:
               p_widgets_for_one_campaign["data"][parent_widget]['global_status'] = "not yet listed" 

    with open(f"../../data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)

    return json.dumps(p_widgets_for_one_campaign)
