from config.config import *
from functions.data_acquisition_functions.get_mgid_widget_clicks_and_costs_by_campaign import get_mgid_widget_clicks_and_costs_by_campaign
from functions.data_acquisition_functions.get_vol_widget_conversions_by_campaign import get_vol_widget_conversions_by_campaign
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
from functions.classification_functions.classify_campaign_for_one_p_widget import classify_campaign_for_one_p_widget
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
from datetime import datetime, timedelta
import json
import os
import sys
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)


def create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range,
        output_name):
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
               p_widgets_for_all_campaigns["data"][parent_widget] = {"for_all_campaigns": {}, "for_each_campaign": []}
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
                p_widgets_for_one_campaign[parent_widget]["vol_id"] = campaign["vol_id"]
                p_widgets_for_one_campaign[parent_widget]["mgid_id"] = campaign["mgid_id"]
                p_widgets_for_one_campaign[parent_widget]["name"] = campaign["name"]
                p_widgets_for_one_campaign[parent_widget]["max_lead_cpa"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[parent_widget]["max_sale_cpa"] = campaign["max_sale_cpa"]

        with open(f'{os.environ.get("ULANMEDIAAPP")}/excluded_p_widgets_lists/{campaign["mgid_id"]}_excluded_p_widgets.json', 'r') as file:
            excluded_widgets = json.load(file)
        pattern = re.compile(r'\d*')

        for p_widget in p_widgets_for_one_campaign:
            if pattern.search(p_widget).group() not in excluded_widgets:
                p_widgets_for_one_campaign[p_widget]["status"] = "included"
            else:
                p_widgets_for_one_campaign[p_widget]["status"] = "excluded"


        # Add each p_widget_for_one_campaign to the list of campaigns for each p widget
        for p_widget in p_widgets_for_one_campaign:
            if p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]


    total_sales = p_widgets_for_all_campaigns["data"][p_widget_id]["for_all_campaigns"]["sales"]
    for campaign in p_widgets_for_all_campaigns["data"][p_widget_id]["for_each_campaign"]:
        classification = classify_campaign_for_one_p_widget(campaign, total_sales)
        campaign["classification"] = classification

    complete_widget_data = {"metadata":
            p_widgets_for_all_campaigns["metadata"], "data":
            p_widgets_for_all_campaigns["data"][p_widget_id]["for_each_campaign"]}

    with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        json.dump(complete_widget_data, file)

    return json.dumps(complete_widget_data)

# old function
# def create_campaigns_for_one_p_widget_dataset(parent_widget_id, date_range, output_name):
    # widget_whitelist = get_whitelist()
    # widget_greylist = get_greylist()
    # widget_blacklist = get_blacklist()


    # parent_widget_global_status = ""
    # if parent_widget_id in widget_whitelist:
       # parent_widget_global_status = "whitelist" 
    # elif parent_widget_id in widget_greylist:
       # parent_widget_global_status = "greylist" 
    # elif parent_widget_id in widget_blacklist:
       # parent_widget_global_status = "blacklist" 
    # else:
       # parent_widget_global_status = "not yet listed" 

    # campaigns = get_campaign_sets()

    # widget_data = {"metadata": {"mgid_start_date": "",
                               # "mgid_end_date": "",
                               # "vol_start_date": "",
                               # "vol_end_date": ""
                               # },
                    # "data": []
                  # } 

    # for campaign in campaigns:
        # vol_id = campaign["vol_id"]
        # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             # json_file = json.load(file)

        # metadata = json_file["metadata"]
        # data = json_file["data"]

        # # add metadata
        # if not widget_data["metadata"]["mgid_start_date"]:
             # widget_data["metadata"]["mgid_start_date"] = metadata["mgid_start_date"]
        # if not widget_data["metadata"]["mgid_end_date"]:
             # widget_data["metadata"]["mgid_end_date"] = metadata["mgid_end_date"]
        # if not widget_data["metadata"]["vol_start_date"]:
             # widget_data["metadata"]["vol_start_date"] = metadata["vol_start_date"]
        # if not widget_data["metadata"]["vol_end_date"]:
             # widget_data["metadata"]["vol_end_date"] = metadata["vol_end_date"]

        # # add widget data
        # widget_ids_with_matching_parent = []
        # for widget_id in list(data.keys()):
            # if widget_id.startswith(parent_widget_id):
                # widget_ids_with_matching_parent.append(widget_id)

        # # 1/24/19 This is for updating the campaign status on each submit
        # # press on campaigns_for_one_p_widget
        # # get list of excluded widgets
        # with open(f'{os.environ.get("ULANMEDIAAPP")}/excluded_p_widgets_lists/{campaign["mgid_id"]}_excluded_p_widgets.json', 'r') as file:
             # excluded_widgets = json.load(file)
        # # regex for extracting parent widget id
        # pattern = re.compile(r'\d*')

        # parent_widget_data = {}
        # for widget_id in widget_ids_with_matching_parent:
            # if pattern.search(widget_id).group() not in excluded_widgets:
                # widget_status = "included" 
            # else:
                # widget_status = "excluded" 

            # if not parent_widget_data:
                # parent_widget_data = {
                # "widget_id": parent_widget_id, 
                # "vol_id": campaign["vol_id"],
                # "mgid_id": campaign["mgid_id"],
                # "name": campaign["name"],
                # "max_lead_cpa": campaign["max_lead_cpa"],
                # "max_sale_cpa": campaign["max_sale_cpa"],
                # "status": widget_status,
                # "global_status": parent_widget_global_status,
                # "clicks": data[widget_id]["clicks"], 
                # "cost": data[widget_id]["cost"],
                # "sales": data[widget_id]["sales"],
                # "leads": data[widget_id]["leads"],
                # "revenue": data[widget_id]["revenue"],
                # }
            # else:
                # parent_widget_data["clicks"] += data[widget_id]["clicks"]
                # parent_widget_data["cost"] += data[widget_id]["cost"]
                # parent_widget_data["sales"] += data[widget_id]["sales"]
                # parent_widget_data["leads"] += data[widget_id]["leads"]
                # parent_widget_data["revenue"] += data[widget_id]["revenue"]

        # if parent_widget_data:
            # # this is where each campaign is classified as good, half good,
            # # bad, half bad, wait
            # parent_widget_data["classification"] = classify_campaign_for_one_p_widget(parent_widget_data )
            # widget_data["data"].append(parent_widget_data)
            
    # complete_widget_data = widget_data 

    # with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        # json.dump(complete_widget_data, file)

    # return json.dumps(complete_widget_data)

