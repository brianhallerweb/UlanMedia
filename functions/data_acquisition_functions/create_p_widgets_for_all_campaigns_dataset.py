from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.classification_functions.classify_campaign_for_one_p_widget import classify_campaign_for_one_p_widget
from functions.classification_functions.classify_p_widget_for_all_campaigns import classify_p_widget_for_all_campaigns
import re
import os
import sys
import json

def create_p_widgets_for_all_campaigns_dataset(date_range):
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
        # 1/14/19 I'm not sure why I have to load the file again here but I was
        # having some unexpected results when I tried to reuse the file data
        # that was loaded in the previous step. It's as if that data was
        # mutated in some way, but I don't see how that is possible. Anyway, it
        # works properly when I reload the data at this step. 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

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
                p_widgets_for_one_campaign[parent_widget]["max_lead_cpa"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[parent_widget]["max_sale_cpa"] = campaign["max_sale_cpa"]
                

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
        total_sales = p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["sales"]
        for campaign in p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/wait
            # counts are recorded
            classification = classify_campaign_for_one_p_widget(campaign, total_sales)
            if classification == "good":
               p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] += 1
            elif classification == "half good": 
               p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] += .5 
            elif classification == "bad": 
               p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] += 1 
            elif classification == "half bad": 
               p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] += .5 
            elif classification == "wait": 
               p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] += 1
                    
    ############################################################
    # At this point, p_widgets_for_all_campaigns["data"] includes good/bad/wait
    # campaign counts for each p widget. Using those counts, the classify the p widget into white/grey/black following the flow chart

    for p_widget in p_widgets_for_all_campaigns["data"].values():
        p_widget["for_all_campaigns"]["classification"] = classify_p_widget_for_all_campaigns(p_widget)

    # The final step is to remove "for_each_campaign" "good_campaigns_count"
    # "bad_campaigns_count" and "wait_campaigns_count" from each widget
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["good_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["bad_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["wait_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget] = p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]

    with open(f"../../data/p_widgets_for_all_campaigns/{date_range}_p_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_all_campaigns, file)

    return json.dumps(p_widgets_for_all_campaigns)
