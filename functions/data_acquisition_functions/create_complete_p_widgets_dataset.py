from config.config import *
from functions.classification_functions.classify_campaign_for_one_p_or_c_widget import classify_campaign_for_one_p_or_c_widget
from functions.classification_functions.classify_p_widget_for_all_campaigns import classify_p_widget_for_all_campaigns
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
import json
import os
import re

def create_complete_p_widgets_dataset(date_range, output_name):

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    ########################################################

    # 2. set up the basic data structure you want to create

    complete_p_widgets = {}

    #########################################################

    # 3. create the "for_all_campaigns" part of each p widget

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        pattern = re.compile(r'\d*')

        for widget in json_file["data"]:
           p_widget = pattern.search(widget).group()
           if p_widget in complete_p_widgets:
               complete_p_widgets[p_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               complete_p_widgets[p_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               complete_p_widgets[p_widget] = {"for_all_campaigns": {}}
               complete_p_widgets[p_widget]["for_all_campaigns"] = json_file["data"][widget]
               complete_p_widgets[p_widget]["for_all_campaigns"]["widget_id"] = p_widget

               if p_widget in widget_whitelist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_whitelist" 
               elif p_widget in widget_greylist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_greylist" 
               elif p_widget in widget_blacklist:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "p_blacklist" 
               else:
                   complete_p_widgets[p_widget]["for_all_campaigns"]['global_status'] = "not yet listed" 

           if widget is not p_widget:
               complete_p_widgets[p_widget]["for_all_campaigns"]["has_children"] = True
           else:
               complete_p_widgets[p_widget]["for_all_campaigns"]["has_children"] = False


    #########################################################

    # 4.  create the "for_each_campaign" part of each p widget
    
    for p_widget in complete_p_widgets:
        complete_p_widgets[p_widget]["for_each_campaign"] = []
    
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        mpc_pattern = re.compile(r'.*cpc_(.*)')
        p_widgets_for_one_campaign = {}
        for widget in json_file["data"]:
            p_widget = pattern.search(widget).group()
            if p_widget in p_widgets_for_one_campaign:
                p_widgets_for_one_campaign[p_widget]["clicks"] += json_file["data"][widget]["clicks"]
                p_widgets_for_one_campaign[p_widget]["cost"] += json_file["data"][widget]["cost"]
                p_widgets_for_one_campaign[p_widget]["revenue"] += json_file["data"][widget]["revenue"]
                p_widgets_for_one_campaign[p_widget]["leads"] += json_file["data"][widget]["leads"]
                p_widgets_for_one_campaign[p_widget]["sales"] += json_file["data"][widget]["sales"]
            else:
                p_widgets_for_one_campaign[p_widget] = json_file["data"][widget]
                p_widgets_for_one_campaign[p_widget]["widget_id"] = p_widget
                p_widgets_for_one_campaign[p_widget]["vol_id"] = campaign["vol_id"]
                p_widgets_for_one_campaign[p_widget]["mgid_id"] = campaign["mgid_id"]
                p_widgets_for_one_campaign[p_widget]["name"] = campaign["name"]
                p_widgets_for_one_campaign[p_widget]["mpl"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[p_widget]["mps"] = campaign["max_sale_cpa"]
                res = mpc_pattern.findall(campaign["name"])
                p_widgets_for_one_campaign[p_widget]["mpc"] = list(res)[0]


        for p_widget in p_widgets_for_one_campaign:
            if complete_p_widgets[p_widget]["for_each_campaign"]:
                complete_p_widgets[p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                complete_p_widgets[p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]

    #################################################################33
     
    # 5. Create the "campaign_counts" part of each p widget
    
    for p_widget in complete_p_widgets:
        complete_p_widgets[p_widget]["good_campaigns_count"] = 0
        complete_p_widgets[p_widget]["bad_campaigns_count"] = 0
        complete_p_widgets[p_widget]["wait_campaigns_count"] = 0

    for p_widget in complete_p_widgets:
        total_sales = complete_p_widgets[p_widget]["for_all_campaigns"]["sales"]
        for campaign in complete_p_widgets[p_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/wait
            # counts are recorded
            classification = classify_campaign_for_one_p_or_c_widget(campaign, total_sales)
            campaign["classification"] = classification
            if classification == "good":
               complete_p_widgets[p_widget]["good_campaigns_count"] += 1
            elif classification == "half good": 
               complete_p_widgets[p_widget]["good_campaigns_count"] += .5 
            elif classification == "bad": 
               complete_p_widgets[p_widget]["bad_campaigns_count"] += 1 
            elif classification == "half bad": 
               complete_p_widgets[p_widget]["bad_campaigns_count"] += .5 
            elif classification == "wait": 
               complete_p_widgets[p_widget]["wait_campaigns_count"] += 1

    #############################################################

    # 6. create the classification of each p widget

    for p_widget in complete_p_widgets.values():
        p_widget["for_all_campaigns"]["classification"] = classify_p_widget_for_all_campaigns(p_widget)

    ############################################################

    # 7. Save complete_p_widgets to a json file and return it as a
    # json file 

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_p_widgets/{output_name}.json", "w") as file:
        json.dump(complete_p_widgets, file)

    return complete_p_widgets
