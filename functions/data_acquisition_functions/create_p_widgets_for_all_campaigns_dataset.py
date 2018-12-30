import json
from functions.misc.get_campaign_sets import get_campaign_sets 
import re
import sys
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist

def create_p_widgets_for_all_campaigns_dataset(date_range):

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    p_widgets_for_all_campaigns = {"metadata":{}, "data":{}}

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        p_widgets_for_all_campaigns["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
        p_widgets_for_all_campaigns["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
        p_widgets_for_all_campaigns["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
        p_widgets_for_all_campaigns["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

        pattern = re.compile(r'\d*')

        for widget in json_file["data"]:
           parent_widget = pattern.search(widget).group()
           if parent_widget in p_widgets_for_all_campaigns["data"]:
               p_widgets_for_all_campaigns["data"][parent_widget]["clicks"] += json_file["data"][widget]["clicks"]
               p_widgets_for_all_campaigns["data"][parent_widget]["cost"] += json_file["data"][widget]["cost"]
               p_widgets_for_all_campaigns["data"][parent_widget]["revenue"] += json_file["data"][widget]["revenue"]
               p_widgets_for_all_campaigns["data"][parent_widget]["leads"] += json_file["data"][widget]["leads"]
               p_widgets_for_all_campaigns["data"][parent_widget]["sales"] += json_file["data"][widget]["sales"]
           else:
               p_widgets_for_all_campaigns["data"][parent_widget] = json_file["data"][widget]
               p_widgets_for_all_campaigns["data"][parent_widget]["widget_id"] = parent_widget
               if parent_widget in widget_whitelist:
                   p_widgets_for_all_campaigns["data"][parent_widget]['global_status'] = "whitelist" 
               elif parent_widget in widget_greylist:
                   p_widgets_for_all_campaigns["data"][parent_widget]['global_status'] = "greylist" 
               elif parent_widget in widget_blacklist:
                   p_widgets_for_all_campaigns["data"][parent_widget]['global_status'] = "blacklist" 
               else:
                   p_widgets_for_all_campaigns["data"][parent_widget]['global_status'] = "not yet listed" 

           if widget is not parent_widget:
               p_widgets_for_all_campaigns["data"][parent_widget]["has_children"] = True
           else:
               p_widgets_for_all_campaigns["data"][parent_widget]["has_children"] = False
        

    with open(f"../../data/p_widgets_for_all_campaigns/{date_range}_p_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_all_campaigns, file)

    return json.dumps(p_widgets_for_all_campaigns)
