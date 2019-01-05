from config.config import *
import json
import re
import os
import sys
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign

def create_c_widgets_for_one_p_widget_dataset(p_widget, date_range):
    # 1/1/19 global status is added here, as opposed to on create_p_and_c_widgets for
    # one campaign so that it will update everytime the submit button is
    # clicked rather than only once every day. 
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()
    # excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id,
            # mgid_id)
    # if p_widget in excluded_widgets:
        # p_widget_status = "excluded"
    # else:
        # p_widget_status = "included"

    p_widget_global_status = ""
    if p_widget in widget_whitelist:
       p_widget_global_status = "whitelist" 
    elif p_widget in widget_greylist:
       p_widget_global_status = "greylist" 
    elif p_widget in widget_blacklist:
       p_widget_global_status = "blacklist" 
    else:
       p_widget_global_status = "not yet listed" 

    c_widgets_for_one_p_widget = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}
                                } 

    campaigns = get_campaign_sets()
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        metadata = json_file["metadata"]
        data = json_file["data"]
    
        if not c_widgets_for_one_p_widget["metadata"]["mgid_start_date"]:
            c_widgets_for_one_p_widget["metadata"]["mgid_start_date"] = metadata["mgid_start_date"]
        if not c_widgets_for_one_p_widget["metadata"]["mgid_end_date"]:
            c_widgets_for_one_p_widget["metadata"]["mgid_end_date"] = metadata["mgid_end_date"]
        if not c_widgets_for_one_p_widget["metadata"]["vol_start_date"]:
           c_widgets_for_one_p_widget["metadata"]["vol_start_date"] = metadata["vol_start_date"]
        if not c_widgets_for_one_p_widget["metadata"]["vol_end_date"]:
           c_widgets_for_one_p_widget["metadata"]["vol_end_date"] = metadata["vol_end_date"]


        pattern = re.compile(r'\d*')
        for widget in data:
           extracted_p_widget = pattern.search(widget).group()
           if extracted_p_widget != p_widget:
               continue;
           if widget in c_widgets_for_one_p_widget["data"]:
               c_widgets_for_one_p_widget["data"][widget]["clicks"] += data[widget]["clicks"]
               c_widgets_for_one_p_widget["data"][widget]["cost"] += data[widget]["cost"]
               c_widgets_for_one_p_widget["data"][widget]["revenue"] += data[widget]["revenue"]
               c_widgets_for_one_p_widget["data"][widget]["leads"] += data[widget]["leads"]
               c_widgets_for_one_p_widget["data"][widget]["sales"] += data[widget]["sales"]
           else:
               c_widgets_for_one_p_widget["data"][widget] = data[widget]
               # c_widgets_for_one_p_widget["data"][widget]["status"] = status
               c_widgets_for_one_p_widget["data"][widget]["global_status"] = p_widget_global_status
               c_widgets_for_one_p_widget["data"][widget]["vol_id"] = metadata["vol_id"]
               c_widgets_for_one_p_widget["data"][widget]["mgid_id"] = metadata["vol_id"]
               c_widgets_for_one_p_widget["data"][widget]["max_lead_cpa"] = metadata["max_lead_cpa"]
               c_widgets_for_one_p_widget["data"][widget]["max_sale_cpa"] = metadata["max_sale_cpa"]

    with open(f"../../data/c_widgets_for_one_p_widget/{p_widget}_{date_range}_c_widgets_for_one_p_widget_dataset.json", "w") as file:
        json.dump(c_widgets_for_one_p_widget, file)
    
    return json.dumps(c_widgets_for_one_p_widget)

