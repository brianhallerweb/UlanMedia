from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets 
import json
import re
import os
import sys

def create_c_widgets_for_one_p_widget_dataset(p_widget, date_range):
    # This function creates a c_widgets_for_one_p_widget json data structure.
    # That means each row is a c widget for a given p widget. The final data
    # structure looks like this:

    # {"metadata": {"mgid_start_date": "2018-07-05",
    #               "mgid_end_date": "2018-12-31",
    #               "vol_start_date": "2018-07-05",
    #               "vol_end_date": "2019-01-01"},
    #  "data    ": {"5633835s713950": {"widget_id": "5633835s713950",
    #                                  "clicks": 20,
    #                                  "cost": 1.06,
    #                                  "revenue": 0.0,
    #                                  "leads": 0,
    #                                  "sales": 0,
    #                                  "referrer": [],
    #                                  "vol_id": "39eded96-4619-4c00-b0e6-bfdc622c894c",
    #                                  "mgid_id": "39eded96-4619-4c00-b0e6-bfdc622c894c",
    #                                  "max_lead_cpa": 5,
    #                                  "max_sale_cpa": 150},
    #     ...
    #     ...
    #     ...

    ########################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()

    ########################################################

    # 2. set up the basic data structure you want to create

    c_widgets_for_one_p_widget = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}

                                } 

    ########################################################
    
    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    c_widgets_for_one_p_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    c_widgets_for_one_p_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    c_widgets_for_one_p_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    c_widgets_for_one_p_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    # At this point in the process, c_widgets_for_one_p_widget looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': {}
    #  }

    ########################################################

    # 4. loop through p and c widgets for one campaign and create c widgets for
    # one p widget

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        data = json_file["data"]
    
        pattern = re.compile(r'\d*')
        mpc_pattern = re.compile(r'.*cpc_(.*)')
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
               c_widgets_for_one_p_widget["data"][widget]["vol_id"] = campaign["vol_id"]
               c_widgets_for_one_p_widget["data"][widget]["mgid_id"] = campaign["mgid_id"]
               c_widgets_for_one_p_widget["data"][widget]["mpl"] = campaign["max_lead_cpa"]
               c_widgets_for_one_p_widget["data"][widget]["mps"] = campaign["max_sale_cpa"]
               res = mpc_pattern.findall(campaign["name"])
               c_widgets_for_one_p_widget["data"][widget]["mpc"] = list(res)[0]

    ############################################################
    # 5. Save c_widgets_for_one_p_widget to a json file and return it as a
    # json file 


    with open(f"../../data/c_widgets_for_one_p_widget/{p_widget}_{date_range}_c_widgets_for_one_p_widget_dataset.json", "w") as file:
        json.dump(c_widgets_for_one_p_widget, file)
    
    return json.dumps(c_widgets_for_one_p_widget)

