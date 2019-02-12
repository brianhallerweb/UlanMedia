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
    # The goal of this function is to return a json dataset for
    # p_widgets_for_all_campaigns. That means each row is a p_widget and each
    # column is data for all campaigns in that p widget.
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
    #                     "global_status": "not yet listed",
    #                     "has_children": "false",
    #                     "classification": "wait",
    #                     "good_campaigns_count": 0,
    #                     "bad_campaigns_count": 0,
    #                     "wait_campaigns_count": 18},
    #           "15865": {...},
    #           .
    #           .
    #           .
    #           }
    # }
    ########################################################

    # 1. get some prerequisite data

    campaigns = get_campaign_sets()
    widget_whitelist = get_whitelist()
    widget_greylist = get_greylist()
    widget_blacklist = get_blacklist()

    ########################################################

    # 2. set up the basic data structure you want to create

    p_widgets_for_all_campaigns = {"metadata":{}, "data":{}}

    #########################################################

    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    p_widgets_for_all_campaigns["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    p_widgets_for_all_campaigns["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    p_widgets_for_all_campaigns["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    p_widgets_for_all_campaigns["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': {}
    #  }

    #########################################################

    # 4. Loop through each campaign to accumulate the most of the data for
    # p_widgets_for_all_campaigns. This step will create
    # p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]
    # The reason for the key "for_all_campaigns" is that there needs to
    # temporarily be other keys as well. In the next few steps, I will create
    # these keys: "for_all_campaigns", "for_each_campaign",
    # "good_campaigns_count", "bad_campaigns_count", and
    # "wait_campaigns_count".

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

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
               p_widgets_for_all_campaigns["data"][parent_widget] = {"for_all_campaigns": {}}
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
               

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'}}, 
    #              '123456': { 'for_all_campaigns : {data...}}
    #              ...
    #              ...
    #              ...
    #            },

    #########################################################

    # 5. Loop through each p widget in p_widgets_for_all_campaigns to create
    # the data stucture (list) to hold
    # "for_each_campaign"
    
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"] = []
    
    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'},
    #                         'for_each_campaign': []}, 
    #              '123456': { 'for_all_campaigns : {data...},
    #                          'for_each_campaign': []}, 
    #              ...
    #              ...
    #              ...
    #            },

    #########################################################
    # 6. loop through each campaign to accumulate and add the data for
    # p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
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
                p_widgets_for_one_campaign[parent_widget]["mpl"] = campaign["max_lead_cpa"]
                p_widgets_for_one_campaign[parent_widget]["mps"] = campaign["max_sale_cpa"]
                

        # Add each p_widget_for_one_campaign to the list of campaigns for each p widget
        for p_widget in p_widgets_for_one_campaign:
            if p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"].append(p_widgets_for_one_campaign[p_widget])
            else:
                p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"] = [p_widgets_for_one_campaign[p_widget]]

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]}, 
    #              '123456': { 'for_all_campaigns : {data...},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]}, 
    #              ...
    #              ...
    #              ...
    #            },
    #################################################################33
     
    # 7. Loop through each p widget in p_widgets_for_all_campaigns to create
    # the data stucture to hold "good_campaigns_count", "bad_campaigns_count",
    # and "wait_campaigns_count"
    
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] = 0
        p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] = 0
        p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] = 0

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 0, 
    #                         'bad_campaigns_count': 0, 
    #                         'wait_campaigns_count': 0, 
    #                       }, 
    #              '123456': { 'for_all_campaigns : {data...},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 0, 
    #                         'bad_campaigns_count': 0, 
    #                         'wait_campaigns_count': 0, 
    #                        }, 
    #              ...
    #              ...
    #              ...
    #            },
     
    #################################################################33

    # 8. loop through each campaign in p_widgets_for_all_campaigns["data"][p_widget]["for_each_campaign"]
    # and add good_campaigns_count, bad_campaigns_count, and wait_campaigns_count
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

    # At this point in the process, p_widgets_for_all_campaigns looks like this
    # (the good/bad/wait counts are filled in):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5, 
    #                       }, 
    #              '123456': { 'for_all_campaigns : {data...},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5, 
    #                        }, 
    #              ...
    #              ...
    #              ...
    #            },
                    
    #############################################################

    # 9. loop through each p widget in p_widgets_for_all_campaigns["data"] and
    # add its classification (white/grey/black) into p_widget["for_all_campaigns"]

    for p_widget in p_widgets_for_all_campaigns["data"].values():
        p_widget["for_all_campaigns"]["classification"] = classify_p_widget_for_all_campaigns(p_widget)

    # At this point in the process, p_widgets_for_all_campaigns looks like this
    # ("for_all_campaigns" has a "classification" key):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'classification': 'wait',
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'has_children': False,
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5, 
    #                       }, 
    #              '123456': { 'for_all_campaigns : {data...},
    #                         'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5, 
    #                        }, 
    #              ...
    #              ...
    #              ...
    #            },

    ##############################################################

    # 10. remove "for_each_campaign" "good_campaigns_count" "bad_campaigns_count" and 
    # "wait_campaigns_count" from each widget and add "good_campaigns_count" "bad_campaigns_count"
    # and "wait_campaigns_count" to p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]
    for p_widget in p_widgets_for_all_campaigns["data"]:
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["good_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["good_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["bad_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["bad_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]["wait_campaigns_count"] = p_widgets_for_all_campaigns["data"][p_widget]["wait_campaigns_count"] 
        p_widgets_for_all_campaigns["data"][p_widget] = p_widgets_for_all_campaigns["data"][p_widget]["for_all_campaigns"]

    # At this point in the process, p_widgets_for_all_campaigns looks like this
    # ("for_all_campaigns" has a "classification" key):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897':  { 'clicks': 8,
    #                         'classification': 'wait',
    #                         'cost': 0.16,
    #                         'global_status': 'not yet listed',
    #                         'has_children': False,
    #                         'leads': 0,
    #                         'referrer': [],
    #                         'revenue': 0.0,
    #                         'sales': 0,
    #                         'widget_id': '986897',
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5,},
    #             '986123':  { 'clicks': 8,
    #                         'classification': 'wait',
    #                         'cost': 0.16,
    #                         'global_status': 'not yet listed',
    #                         'has_children': False,
    #                         'leads': 0,
    #                         'referrer': [],
    #                         'revenue': 0.0,
    #                         'sales': 0,
    #                         'widget_id': '986897',
    #                         'good_campaigns_count': 5, 
    #                         'bad_campaigns_count': 5, 
    #                         'wait_campaigns_count': 5, 
    #                       }, 
    #              ...
    #              ...
    #              ...
    #            },

    ############################################################
    # 11. Save p_widgets_for_all_campaigns to a json file and return it as a
    # json file 

    with open(f"../../data/p_widgets_for_all_campaigns/{date_range}_p_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_all_campaigns, file)

    return json.dumps(p_widgets_for_all_campaigns)




