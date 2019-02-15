from config.config import *
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
import os
import json
import re

def create_p_widgets_for_one_campaign_dataset(mgid_token, vol_id, date_range):
    # The goal of this function is to return a json dataset for
    # p_widgets_for_one_campaign. That means each row is a p_widget and each
    # column is data for one campaign. 
    #
    # The resulting data structure looks like this:
    # {"metadata": {"mgid_start_date": "2018-08-09",
    #               "mgid_end_date": "2019-02-04",
    #               "vol_start_date": "2018-08-09",
    #               "vol_end_date": "2019-02-05"},
    #  "data": {"21391": {"widget_id": "21391",
    #                     "clicks": 140,
    #                     "cost": 3.0,
    #                     "revenue": 0.0,
    #                     "leads": 5,
    #                     "sales": 0,
    #                     "referrer": ["mgid.com"],
    #                     "mpc": ...,
    #                     "mpl": ...,
    #                     "mps": ...,
    #                     "status": "included"
    #                     "global_status": "not yet listed",
    #           "15865": {...},
    #           .
    #           .
    #           .
    #           }
    # }
    ########################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()

    mgid_id = ""
    mpc = ""
    mpl = ""
    mps = ""
    mpc_pattern = re.compile(r'.*cpc_(.*)')
    for campaign in campaigns:
        if campaign["vol_id"] == vol_id:
            mgid_id = campaign["mgid_id"]
            res = mpc_pattern.findall(campaign["name"])
            mpc = list(res)[0]
            mpl = campaign["max_lead_cpa"]
            mps = campaign["max_sale_cpa"]

    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    with open(f'{os.environ.get("ULANMEDIAAPP")}/excluded_p_widgets_lists/{mgid_id}_excluded_p_widgets.json', 'r') as file:
        excluded_widgets = json.load(file)

    ########################################################

    # 2. set up the basic data structure you want to create

    p_widgets_for_one_campaign = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}
                                } 

    ########################################################
    
    # 3. add the metadata

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
       json_file = json.load(file)

    p_widgets_for_one_campaign["metadata"] = json_file["metadata"]

    ########################################################

    # 4. loop through p and c widgets for one campaign and create p widgets for
    # one campaign

    data = json_file["data"]

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
           p_widgets_for_one_campaign["data"][parent_widget]["vol_id"] = vol_id
           p_widgets_for_one_campaign["data"][parent_widget]["mgid_id"] = mgid_id
           p_widgets_for_one_campaign["data"][parent_widget]["widget_id"] = parent_widget
           p_widgets_for_one_campaign["data"][parent_widget]["mpc"] = mpc 
           p_widgets_for_one_campaign["data"][parent_widget]["mpl"] = mpl 
           p_widgets_for_one_campaign["data"][parent_widget]["mps"] = mps 

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

    ############################################################

    # 5. Save p_widgets_for_all_campaigns to a json file and return it as a
    # json file 

    with open(f"../../data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)

    return json.dumps(p_widgets_for_one_campaign)
