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

def create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range,
        output_name):

    # The goal of this function is to return a json dataset for
    # campaigns_for_one_p_widget. That means each row is a campaign and each
    # column is data for that one campaign in one p widget.
    #
    # The resulting data structure looks like this:
    #{"metadata": {"mgid_start_date": "2018-07-18",
    #              "mgid_end_date": "2019-01-13",
    #              "vol_start_date": "2018-07-18",
    #              "vol_end_date": "2019-01-14"},
    # "data": [{"widget_id": "670024",
    #           "vol_id": "dc1351fe-b55a-49a6-a679-e04539ff1840",
    #           "mgid_id": "527378",
    #           "name": "bin_australia_all_desktop_cpc_0.07",
    #           "mpl": 10,
    #           "mps": 300,
    #           "status": "included",
    #           "global_status": "not yet listed",
    #           "clicks": 2,
    #           "cost": 0.14,
    #           "sales": 0,
    #           "leads": 0,
    #           "revenue": 0.0,
    #           "classification": "wait"},
    #           {"widget_id": "670024",
    #            "vol_id": "4ff2a836-8790-4e07-9f45-98b05c3a393a",
    #            "mgid_id": "527382",
    #            "name": "bin_canada_all_desktop_cpc_0.07",
    #            "mpl": 10,
    #            "mpl": 300,
    #            "status": "included",
    #            "global_status": "not yet listed",
    #            "clicks": 7,
    #            "cost": 0.49,
    #            "sales": 0,
    #            "leads": 0,
    #            "revenue": 0.0,
    #            "classification": "wait"},
    #            {....},
    #             .
    #             .
    #             .
    #            ] 
    #######################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    ########################################################

    # 2. set up a basic data structure for campaigns_for_one_p_widget

    campaigns_for_one_p_widget = {"metadata":{}, "data":[]}

    #########################################################

    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    campaigns_for_one_p_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    campaigns_for_one_p_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    campaigns_for_one_p_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    campaigns_for_one_p_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': [] 
    #  }

    #########################################################
    
    # 4. This step is a little tricky. In order to classify each campaign in
    # campaign_for_one_p_widget["data"], I need data on all campaigns in that p
    # widget. So the temporary data structure will look like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': 'for_all_campaigns': {},
    #          'for_each_campaign': [] 
    #  }

    campaigns_for_one_p_widget["data"] = {"for_all_campaigns": {},
            "for_each_campaign": []}

    # To find campaigns_for_one_p_widget["data"]["for_all_campaigns"] and 
    # campaigns_for_one_p_widget["data"]["for_all_campaigns"], it is actually
    # easist to recreate p_widgets_for_all_campaigns. 
    #
    # So the temporary data structure that will be build on sub-steps of step 4
    # looks like this:
    # p_widgets_for_all_campaigns[parent_widget] = {"for_all_campaigns": {row data
    # for p_widgets_for_all_campaigns page}, 
    #                                         "for_each_campaign": [{row
    #                                             data for
    #                                             campaigns_for_one_p_widget
    #                                             page}, {}, ...], 
    # }

    ######################################################
    
    # 4a. create the data basic structure
    p_widgets_for_all_campaigns = {}
    
    ####################################################

    # 4b. Loop through each campaign to accumulate the data for
    # p_widgets_for_all_campaigns[p_widget]["for_all_campaigns"]

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        pattern = re.compile(r'\d*')

        for widget in json_file["data"]:
           parent_widget = pattern.search(widget).group()
           if parent_widget in p_widgets_for_all_campaigns:
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               p_widgets_for_all_campaigns[parent_widget] = {"for_all_campaigns": {}}
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"] = json_file["data"][widget]
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["widget_id"] = parent_widget

               if parent_widget in widget_whitelist:
                   p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "whitelist" 
               elif parent_widget in widget_greylist:
                   p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "greylist" 
               elif parent_widget in widget_blacklist:
                   p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "blacklist" 
               else:
                   p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]['global_status'] = "not yet listed" 

           if widget is not parent_widget:
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["has_children"] = True
           else:
               p_widgets_for_all_campaigns[parent_widget]["for_all_campaigns"]["has_children"] = False

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    #  '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                               'cost': 0.16,
    #                               'global_status': 'not yet listed',
    #                               'has_children': False,
    #                               'leads': 0,
    #                               'referrer': [],
    #                               'revenue': 0.0,
    #                               'sales': 0,
    #                               'widget_id': '986897'} }


    ####################################

    # 4c. Create the data structure for p_widgets_for_all_campaigns[parent_widget]["for_each_campaign"]

    for parent_widget in p_widgets_for_all_campaigns:
        p_widgets_for_all_campaigns[parent_widget]["for_each_campaign"] = []

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    #  '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                               'cost': 0.16,
    #                               'global_status': 'not yet listed',
    #                               'has_children': False,
    #                               'leads': 0,
    #                               'referrer': [],
    #                               'revenue': 0.0,
    #                               'sales': 0,
    #                               'widget_id': '986897'}
    #              'for_each_campaign: []
    #            }

    #########################################################
    # 4d. loop through each campaign to accumulate and add the data for
    # p_widgets_for_all_campaigns[p_widget]["for_each_campaign"]

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        mpc_pattern = re.compile(r'.*cpc_(.*)')
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
                p_widgets_for_one_campaign[parent_widget]["mpl"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[parent_widget]["mps"] = campaign["max_sale_cpa"]
                res = mpc_pattern.findall(campaign["name"])
                p_widgets_for_one_campaign[parent_widget]["mpc"] = list(res)[0]
                
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
            if p_widgets_for_all_campaigns[p_widget]["for_each_campaign"]:
                p_widgets_for_all_campaigns[p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                p_widgets_for_all_campaigns[p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                  'cost': 0.16,
    #                                  'global_status': 'not yet listed',
    #                                  'has_children': False,
    #                                  'leads': 0,
    #                                  'referrer': [],
    #                                  'revenue': 0.0,
    #                                  'sales': 0,
    #                                  'widget_id': '986897'},
    #           'for_each_campaign': [ { 'clicks': 1,
    #                                    'cost': 0.07,
    #                                    'leads': 0,
    #                                    'max_lead_cpa': 10,
    #                                    'max_sale_cpa': 300,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'status': 'included',
    #                                    'widget_id': '986897'},
    #                                  { 'clicks': 1,
    #                                    'cost': 0.03,
    #                                    'leads': 0,
    #                                    'max_lead_cpa': 5,
    #                                    'max_sale_cpa': 300,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'status': 'included',
    #                                    'widget_id': '986897'},
    #                                  { 'clicks': 6,
    #                                    'cost': 0.06,
    #                                    'leads': 0,
    #                                    'max_lead_cpa': 4,
    #                                    'max_sale_cpa': 150,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'status': 'included',
    #                                    'widget_id': '986897'}]}}

    # Step 4 is now complete.

    #########################################

    # 5. Take out the only p widget you care about from
    # p_widgets_for_all_campaigns and put it into campaigns_for_one_p_widget
    campaigns_for_one_p_widget["data"]["for_all_campaigns"] = p_widgets_for_all_campaigns[p_widget_id]["for_all_campaigns"]
    campaigns_for_one_p_widget["data"]["for_each_campaign"] = p_widgets_for_all_campaigns[p_widget_id]["for_each_campaign"]

    # At this point in the process, campaigns_for_one_p_widget looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #   'data': { 'for_all_campaigns': { 'clicks': 28890,
    #                                   'cost': 1221.1599999999357,
    #                                   'global_status': 'greylist',
    #                                   'has_children': True,
    #                                   'leads': 86,
    #                                   'referrer': [],
    #                                   'revenue': 830.0,
    #                                   'sales': 2,
    #                                   'widget_id': '5712706'},
    #            'for_each_campaign': [ { 'clicks': 525,
    #                                     'cost': 5.249999999999994,
    #                                     'leads': 3,
    #                                     'max_lead_cpa': 5,
    #                                     'max_sale_cpa': 150,
    #                                     'referrer': [],
    #                                     'revenue': 330.0,
    #                                     'sales': 1,
    #                                     'status': 'included',
    #                                     'widget_id': '5712706'},
    #                                     {....},
    #                                     .
    #                                     .
    #                                   ]},
    #}
    #######################################

    # 6. Add classifications to each campaign in campaigns_for_one_p_widget["data"]["for_all_campaigns"]
    total_sales = campaigns_for_one_p_widget["data"]["for_all_campaigns"]["sales"]
    for campaign in campaigns_for_one_p_widget["data"]["for_each_campaign"]:
        classification = classify_campaign_for_one_p_widget(campaign, total_sales)
        campaign["classification"] = classification

    # At this point in the process, campaigns_for_one_p_widget looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #   'data': { 'for_all_campaigns': { 'clicks': 28890,
    #                                   'cost': 1221.1599999999357,
    #                                   'global_status': 'greylist',
    #                                   'has_children': True,
    #                                   'leads': 86,
    #                                   'referrer': [],
    #                                   'revenue': 830.0,
    #                                   'sales': 2,
    #                                   'widget_id': '5712706'},
    #            'for_each_campaign': [ { 'clicks': 525,
    #                                     'classification': 'wait'
    #                                     'cost': 5.249999999999994,
    #                                     'leads': 3,
    #                                     'max_lead_cpa': 5,
    #                                     'max_sale_cpa': 150,
    #                                     'referrer': [],
    #                                     'revenue': 330.0,
    #                                     'sales': 1,
    #                                     'status': 'included',
    #                                     'widget_id': '5712706'},
    #                                     {....},
    #                                     .
    #                                     .
    #                                   ]},
    #}
    #######################################

    # 7. Remove "for_all_campaigns" from campaigns_for_one_p_widget
    campaigns_for_one_p_widget["data"] = campaigns_for_one_p_widget["data"]["for_each_campaign"]

    # At this point in the process, campaigns_for_one_p_widget looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #   'data': [ { 'clicks': 525,
    #           'classification': 'wait'
    #           'cost': 5.249999999999994,
    #           'leads': 3,
    #           'mpl': 5,
    #           'mps': 150,
    #           'referrer': [],
    #           'revenue': 330.0,
    #           'sales': 1,
    #           'status': 'included',
    #           'widget_id': '5712706'},
    #           {....},
    #           .
    #           .
    #            ]},
    #}
    #######################################

    # 8. Save campaigns_for_one_p_widget to a json file and return it as json

    with open(f"../../data/campaigns_for_one_p_widget/{output_name}.json", "w") as file:
        json.dump(campaigns_for_one_p_widget, file)

    return json.dumps(campaigns_for_one_p_widget)

