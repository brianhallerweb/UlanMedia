import json
from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
import re
import os
import sys
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist

import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_p_widgets_for_all_campaigns_dataset_with_classification(date_range):
    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    p_widgets_for_all_campaigns = {"metadata":{}, "data":{}}

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        p_widgets_for_all_campaigns["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
        p_widgets_for_all_campaigns["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
        p_widgets_for_all_campaigns["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
        p_widgets_for_all_campaigns["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

        pattern = re.compile(r'\d*')

        # set up the p_widgets_for_all_campaings["data"] data structure and
        # fill in the "for_all_campaigns" value. The data structure looks like
        # this:
        # p_widgets_for_all_campaigns["data"][parent_widget] = {"for_all_campaigns": {row data
        # for p_widgets_for_all_campaigns page}, 
        #                                         "for_each_campaign": [{row
        #                                             data for
        #                                             campaigns_for_one_p_widget
        #                                             page}, {}, ...], 
        #                                        "good_campaigns_count" = 0, 
        #                                        "bad_campaigns_count" = 0, 
        #                                        "wait_campaigns_count" = 0
        # }
        # "for_all_campaigns" means the accumulated data for all the campaigns
        # that include the particular p widget.
        # "for each campaign" is a list of each campaign for one particular p
        # widget
        
        for widget in json_file["data"]:
           parent_widget = pattern.search(widget).group()
           if parent_widget in p_widgets_for_all_campaigns["data"]:
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               p_widgets_for_all_campaigns["data"][parent_widget] = {"for_all_campaigns": {}, "for_each_campaign": [], "good_campaigns_count": 0, "bad_campaigns_count": 0, "wait_campaigns_count": 0}
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"] = json_file["data"][widget]
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["widget_id"] = parent_widget

               if parent_widget in widget_whitelist:
                   p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]['global_status'] = "whitelist" 
               elif parent_widget in widget_greylist:
                   p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]['global_status'] = "greylist" 
               elif parent_widget in widget_blacklist:
                   p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]['global_status'] = "blacklist" 
               else:
                   p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]['global_status'] = "not yet listed" 

           if widget is not parent_widget:
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["has_children"] = True
           else:
               p_widgets_for_all_campaigns["data"][parent_widget]["for_all_campaigns"]["has_children"] = False

        # for each campaign, accumulate c widgets for one p widget together
        # into one p widget
        # The result of this is that p_widgets_for_one_campaign is a dictionary
        # of individual p_widgets in one campaign. 
        p_widgets_for_one_campaign = {}
        for widget in json_file["data"]:
            parent_widget = pattern.search(widget).group()
            if parent_widget in p_widgets_for_one_campaign:
                p_widgets_for_one_campaign[parent_widget]["clicks"] += json_file["data"][widget]["clicks"]
                p_widgets_for_one_campaign[parent_widget]["cost"] += json_file["data"][widget]["cost"]
                p_widgets_for_one_campaign[parent_widget]["revenue"] += json_file["data"][widget]["revenue"]
                p_widgets_for_one_campaign[parent_widget]["leads"] += json_file["data"][widget]["leads"]
                p_widgets_for_one_campaign[parent_widget]["sales"] += json_file["data"][widget]["sales"]
            else:
                p_widgets_for_one_campaign[parent_widget] = json_file["data"][widget]
                p_widgets_for_one_campaign[parent_widget]["widget_id"] = parent_widget
                

        # Add each p_widget_for_one_campaign to the list of campaigns for each p widget
        for p_widget in p_widgets_for_one_campaign:
            if p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]

    ############################################################
    # At this point, p_widgets_for_all_campaigns["data"] is a dictionary of
    # p_widgets, each with accumulated data for all campaigns (the
    # "for_all_campaigns" value) and data for each campaign (the
    # "for_each_campaign" value)
     
    # loop through each campaign for each p widget and determine the
    # good_campaigns_count, bad_campaigns_count, and wait_campaigns_count
    for p_widget in p_widgets_for_all_campaigns["data"]:
        for campaign in p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/wait
            # counts are recorded
            if campaign["clicks"] == 0:
               p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] += 1
               continue
            elif campaign["leads"]/campaign["clicks"]*100 >= 0.25: 
                if campaign["sales"] >= 1:
                    p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] += 1
                    continue
                else:
                    if campaign["leads"] >= 3:
                        p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] += 1
                        continue
                    else:
                        p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] += .5
                        continue
            else:
                if (campaign["cost"] > 30) | (campaign["clicks"] > 700):
                    p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] += 1
                    continue;
                elif ((campaign["cost"] > 10) & (campaign["cost"] < 30)) | ((campaign["clicks"] > 300) & (campaign["clicks"] < 700)):
                    if campaign["leads"] == 0:
                        p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] += .5 
                        continue;
                    else:
                        p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] += 1 
                        continue;
                elif ((campaign["cost"] < 10) | (campaign["clicks"] < 300)):
                    p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] += 1 
                    continue;
                    
    ############################################################
    # At this point, p_widgets_for_all_campaigns["data"] includes good/bad/wait
    # campaign counts for each p widget. Using those counts, the classify the p widget into white/grey/black following the flow chart

    for p_widget in p_widgets_for_all_campaigns["data"].values():
        if (p_widget["for_all_campaigns"]["cost"] >= 10) | (p_widget["for_all_campaigns"]["clicks"] >= 300):
            if (p_widget["good_campaigns_count"] >= 3) & (p_widget["bad_campaigns_count"] == 0):
                p_widget["for_all_campaigns"]["classification"] = "white"
                continue
            elif (p_widget["good_campaigns_count"] > 0) & (p_widget["bad_campaigns_count"] > 0):
                p_widget["for_all_campaigns"]["classification"] = "grey"
                continue
            elif (p_widget["good_campaigns_count"] == 0) & (p_widget["bad_campaigns_count"] >= 3):
                p_widget["for_all_campaigns"]["classification"] = "black"
                continue
            elif (p_widget["good_campaigns_count"] == 0) & (p_widget["bad_campaigns_count"] >= 1) & (p_widget["for_all_campaigns"]["revenue"] - p_widget["for_all_campaigns"]["cost"] < -60):
                p_widget["for_all_campaigns"]["classification"] = "black"
                continue
            else:
                p_widget["for_all_campaigns"]["classification"] = "wait"
                continue
        else:
            if p_widget["for_all_campaigns"]["global_status"] == "not yet listed":
                p_widget["for_all_campaigns"]["classification"] = "wait"
                continue
            else:
                p_widget["for_all_campaigns"]["classification"] = p_widget["for_all_campaigns"]["global_status"]
                continue
            
    # The final step is to remove "for_each_campaign" "good_campaigns_count"
    # "bad_campaigns_count" and "wait_campaigns_count" from each widget
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget] = p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]
        
    
    with open(f"../../data/p_widgets_for_all_campaigns_with_classification/{date_range}_p_widgets_for_all_campaigns_dataset_with_classification.json", "w") as file:
        json.dump(p_widgets_for_all_campaigns, file)

    return json.dumps(p_widgets_for_all_campaigns)
