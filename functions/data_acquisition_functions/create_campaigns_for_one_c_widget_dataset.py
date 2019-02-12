from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
import os
import json
import sys
import re

def create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, output_name):
    # This function creates a campaigns_for_one_one_c_widget json data structure.
    # That means each row is a campaign for a given c widget. The final data
    # structure looks like this:

    #{"metadata": {"mgid_start_date": "2018-09-09",
    #              "mgid_end_date": "2018-12-07",
    #              "vol_start_date": "2018-09-09",
    #              "vol_end_date": "2018-12-08"},
    # "data    ": [{"widget_id": "5705354s737122",
    #               "vol_id": "39eded96-4619-4c00-b0e6-bfdc622c894c",
    #               "mgid_id": "506299",
    #               "name": "bin_argentina_all_desktop_cpc_0.01",
    #               "max_lead_cpa": 5,
    #               "max_sale_cpa": 150,
    #               "status": "included",
    #               "global_status": "greylist",
    #               "clicks": 2,
    #               "cost": 0.02,
    #               "sales": 0,
    #               "leads": 1,
    #               "revenue": 0.0},
    #                ........ 
    #                ........ 
    #                ........ 
    #}

    ########################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()


    # for p_widget in p_widgets_for_one_campaign:
        # if pattern.search(p_widget).group() not in excluded_widgets:
            # p_widgets_for_one_campaign[p_widget]["status"] = "included"
        # else:
            # p_widgets_for_one_campaign[p_widget]["status"] = "excluded"



    #######################################################

    # 2. set up the basic data structure you want to create

    campaigns_for_one_c_widget = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": [] 
                                } 

    ########################################################
    
    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)

    campaigns_for_one_c_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    campaigns_for_one_c_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    campaigns_for_one_c_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    campaigns_for_one_c_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    # At this point in the process, campaigns_for_one_c_widget looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': {}
    #  }

    ########################################################

    # 4. loop through p and c widgets for one campaign and create campaigns for
    # one c widget

    for campaign in campaigns:

        vol_id = campaign["vol_id"]
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
             json_file = json.load(file)
        data = json_file["data"]

        with open(f'{os.environ.get("ULANMEDIAAPP")}/excluded_p_widgets_lists/{campaign["mgid_id"]}_excluded_p_widgets.json', 'r') as file:
            excluded_widgets = json.load(file)

        c_widget_data = {}
        p_widget_pattern = re.compile(r'\d*')
        mpc_pattern = re.compile(r'.*cpc_(.*)')
        for widget in data:
            if widget == c_widget_id:
                res = mpc_pattern.findall(campaign["name"])
                mpc = list(res)[0]
                p_widget = p_widget_pattern.search(widget).group()
                status = ""
                if p_widget in excluded_widgets:
                    status = "excluded"
                else:
                    status = "included"
                c_widget_data = {
                "widget_id": widget, 
                "vol_id": campaign["vol_id"],
                "mgid_id": campaign["mgid_id"],
                "name": campaign["name"],
                "mpc": mpc,
                "mpl": campaign["max_lead_cpa"],
                "mps": campaign["max_sale_cpa"],
                "status": status,
                "clicks": data[widget]["clicks"], 
                "cost": data[widget]["cost"],
                "sales": data[widget]["sales"],
                "leads": data[widget]["leads"],
                "revenue": data[widget]["revenue"],
                }

        if c_widget_data:
            campaigns_for_one_c_widget["data"].append(c_widget_data)
            
    ############################################################
    # 5. Save campaigns_for_one_c_widget to a json file and return it as a
    # json file 

    with open(f"../../data/campaigns_for_one_c_widget/{output_name}.json", "w") as file:
        json.dump(campaigns_for_one_c_widget, file)

    return json.dumps(campaigns_for_one_c_widget)


