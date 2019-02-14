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

import pprint
pp=pprint.PrettyPrinter(indent=2)


def create_c_widgets_for_all_campaigns_dataset(date_range):

    # The goal of this function is to return a json dataset for
    # c_widgets_for_all_campaigns. That means each row is a c_widget and each
    # column is data for all campaigns in that c widget.
    #
    # The resulting data structure looks like this:
    # {"metadata": {"mgid_start_date": "2018-08-09",
    #               "mgid_end_date": "2019-02-04",
    #               "vol_start_date": "2018-08-09",
    #               "vol_end_date": "2019-02-05"},
    #  "data": {"5712706s675450": {"widget_id": "5712706s675450", 
    #                              "clicks": 40, 
    #                              "cost": 1, 
    #                              "revenue": 0.0, 
    #                              "leads": 1, 
    #                              "sales": 0, 
    #                              "referrer": ["mgid.com"],
    #                              "global_status": "not yet listed",
    #                              "classification": "wait",
    #                              "good_campaigns_count": 0,
    #                              "bad_campaigns_count": 0,
    #                              "wait_campaigns_count": 3},
    #           "15777865s675450": {...},
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

    c_widgets_for_all_campaigns = {"metadata":{}, "data":{}}

    #########################################################

    # 3. Add the metadata. The metadata are the date ranges of the mgid and vol
    # request dates. All p_and_c_widgets_for_one_campaign files have the same
    # date ranges so I am just using the first campaign. 

    vol_id_for_adding_metadata = campaigns[0]["vol_id"]
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    c_widgets_for_all_campaigns["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
    c_widgets_for_all_campaigns["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
    c_widgets_for_all_campaigns["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
    c_widgets_for_all_campaigns["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]

    # At this point in the process, c_widgets_for_all_campaigns looks like this:
    #{ 'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    #  'data': {}
    #  }

    #########################################################

    # 4. Loop through each campaign to accumulate the most of the data for
    # c_widgets_for_all_campaigns. This step will create
    # c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]
    # The reason for the key "for_all_campaigns" is that there needs to
    # temporarily be other keys as well. In the next few steps, I will create
    # these keys: "for_all_campaigns", "for_each_campaign",
    # "good_campaigns_count", "bad_campaigns_count", and
    # "wait_campaigns_count".

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        pattern = re.compile(r'.*s.*')

        # set up the c_widgets_for_all_campaings["data"] data structure and
        # fill in the "for_all_campaigns" value. The data structure looks like
        # this:
        # c_widgets_for_all_campaigns["data"][c_widget] = {"for_all_campaigns": {row data
        # for c_widgets_for_all_campaigns page}, 
        #                                         "for_each_campaign": [{row
        #                                             data for
        #                                             campaigns_for_one_c_widget
        #                                             page}, {}, ...], 
        #                                        "good_campaigns_count" = 0, 
        #                                        "bad_campaigns_count" = 0, 
        #                                        "wait_campaigns_count" = 0
        # }
        # "for_all_campaigns" means the accumulated data for all the campaigns
        # that include the particular c widget.
        # "for each campaign" is a list of each campaign for one particular p
        # widget
        
        for widget in json_file["data"]:
           c_widget = pattern.search(widget)
           if c_widget == None:
               continue
           c_widget = c_widget.group()
           if c_widget in c_widgets_for_all_campaigns["data"]:
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["clicks"] += json_file["data"][widget]["clicks"]
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["cost"] += json_file["data"][widget]["cost"]
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["revenue"] += json_file["data"][widget]["revenue"]
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["leads"] += json_file["data"][widget]["leads"]
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["sales"] += json_file["data"][widget]["sales"]
           else:
               c_widgets_for_all_campaigns["data"][c_widget] = {"for_all_campaigns": {}}
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"] = json_file["data"][widget]
               c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["widget_id"] = c_widget

               if c_widget in widget_whitelist:
                   c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]['global_status'] = "whitelist" 
               elif c_widget in widget_greylist:
                   c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]['global_status'] = "greylist" 
               elif c_widget in widget_blacklist:
                   c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]['global_status'] = "blacklist" 
               else:
                   c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]['global_status'] = "not yet listed" 

               

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '5712706s675450': { 'for_all_campaigns': { 'clicks': 8,
    #                                    'cost': 0.16,
    #                                    'global_status': 'not yet listed',
    #                                    'leads': 0,
    #                                    'referrer': [],
    #                                    'revenue': 0.0,
    #                                    'sales': 0,
    #                                    'widget_id': '986897'}}, 
    #            '1234562s453452': { 'for_all_campaigns : {data...}}
    #              ...
    #              ...
    #              ...
    #            },


    #########################################################

    # 5. Loop through each p widget in p_widgets_for_all_campaigns to create
    # the data stucture (list) to hold
    # "for_each_campaign"
    
    for c_widget in c_widgets_for_all_campaigns["data"]:
        c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"] = []
    
    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897s321413': { 'for_all_campaigns': { 'clicks': 8,
    #                                                      'cost': 0.16,
    #                                                      'global_status': 'not yet listed',
    #                                                      'leads': 0,
    #                                                      'referrer': [],
    #                                                      'revenue': 0.0,
    #                                                      'sales': 0,
    #                                                      'widget_id': '986897s321413'},
    #                               'for_each_campaign': []}, 
    #            '123456s132413': { 'for_all_campaigns : {data...},
    #                               'for_each_campaign': []}, 
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

        c_widgets_for_one_campaign = {}
        for widget in json_file["data"]:
            c_widget = pattern.search(widget)
            if c_widget == None:
                continue
            c_widget = c_widget.group()
            if c_widget in c_widgets_for_one_campaign:
                c_widgets_for_one_campaign[c_widget]["clicks"] += json_file["data"][widget]["clicks"]
                c_widgets_for_one_campaign[c_widget]["cost"] += json_file["data"][widget]["cost"]
                c_widgets_for_one_campaign[c_widget]["revenue"] += json_file["data"][widget]["revenue"]
                c_widgets_for_one_campaign[c_widget]["leads"] += json_file["data"][widget]["leads"]
                c_widgets_for_one_campaign[c_widget]["sales"] += json_file["data"][widget]["sales"]
            else:
                c_widgets_for_one_campaign[c_widget] = json_file["data"][widget]
                c_widgets_for_one_campaign[c_widget]["widget_id"] = c_widget
                c_widgets_for_one_campaign[c_widget]["mpl"] = campaign["max_lead_cpa"]
                c_widgets_for_one_campaign[c_widget]["mps"] = campaign["max_sale_cpa"]
                

        # Add each c_widget_for_one_campaign to the list of campaigns for each p widget
        for c_widget in c_widgets_for_one_campaign:
            if c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"]:
                c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"].append(c_widgets_for_one_campaign[c_widget])
            else:
                c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"] = [c_widgets_for_one_campaign[c_widget]]

    # At this point in the process, p_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '86897s5409852': { 'for_all_campaigns': { 'clicks': 8,
    #                                                       'cost': 0.16,
    #                                                       'global_status': 'not yet listed',
    #                                                       'leads': 0,
    #                                                       'referrer': [],
    #                                                       'revenue': 0.0,
    #                                                       'sales': 0,
    #                                                       'widget_id': '86897s5409852'},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]}, 
    #            '123456s532485': { 'for_all_campaigns : {data...},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]}, 
    #              ...
    #              ...
    #              ...
    #            },

    #################################################################33
     
    # 7. Loop through each c widget in c_widgets_for_all_campaigns to create
    # the data stucture to hold "good_campaigns_count", "bad_campaigns_count",
    # and "wait_campaigns_count"
    
    for c_widget in c_widgets_for_all_campaigns["data"]:
        c_widgets_for_all_campaigns["data"][c_widget]["good_campaigns_count"] = 0
        c_widgets_for_all_campaigns["data"][c_widget]["bad_campaigns_count"] = 0
        c_widgets_for_all_campaigns["data"][c_widget]["wait_campaigns_count"] = 0

    # At this point in the process, c_widgets_for_all_campaigns looks like this:
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897s245252': { 'for_all_campaigns': { 'clicks': 8,
    #                                                      'cost': 0.16,
    #                                                      'global_status': 'not yet listed',
    #                                                      'leads': 0,
    #                                                      'referrer': [],
    #                                                      'revenue': 0.0,
    #                                                      'sales': 0,
    #                                                      'widget_id': '986897s245252'},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                               'good_campaigns_count': 0, 
    #                               'bad_campaigns_count': 0, 
    #                               'wait_campaigns_count': 0, 
    #                             }, 
    #            '123456s524543': { 'for_all_campaigns : {data...},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                               'good_campaigns_count': 0, 
    #                               'bad_campaigns_count': 0, 
    #                               'wait_campaigns_count': 0, 
    #                              }, 
    #              ...
    #              ...
    #              ...
    #            },
     
    #################################################################33

    # 8. loop through each campaign in c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"]
    # and add good_campaigns_count, bad_campaigns_count, and wait_campaigns_count
    for c_widget in c_widgets_for_all_campaigns["data"]:
        total_sales = c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["sales"]
        for campaign in c_widgets_for_all_campaigns["data"][c_widget]["for_each_campaign"]:
            # This is where each campaign is classified and the good/bad/wait
            # counts are recorded
            classification = classify_campaign_for_one_p_widget(campaign, total_sales)
            if classification == "good":
               c_widgets_for_all_campaigns["data"][c_widget]["good_campaigns_count"] += 1
            elif classification == "half good": 
               c_widgets_for_all_campaigns["data"][c_widget]["good_campaigns_count"] += .5 
            elif classification == "bad": 
               c_widgets_for_all_campaigns["data"][c_widget]["bad_campaigns_count"] += 1 
            elif classification == "half bad": 
               c_widgets_for_all_campaigns["data"][c_widget]["bad_campaigns_count"] += .5 
            elif classification == "wait": 
               c_widgets_for_all_campaigns["data"][c_widget]["wait_campaigns_count"] += 1

    # At this point in the process, c_widgets_for_all_campaigns looks like this
    # (the good/bad/wait counts are filled in):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '986897s245252': { 'for_all_campaigns': { 'clicks': 8,
    #                                                      'cost': 0.16,
    #                                                      'global_status': 'not yet listed',
    #                                                      'leads': 0,
    #                                                      'referrer': [],
    #                                                      'revenue': 0.0,
    #                                                      'sales': 0,
    #                                                      'widget_id': '986897s245252'},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                               'good_campaigns_count': 1, 
    #                               'bad_campaigns_count': 1, 
    #                               'wait_campaigns_count': 1, 
    #                       }, 
    #            '123456s498527': { 'for_all_campaigns : {data...},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                               'good_campaigns_count': 1, 
    #                               'bad_campaigns_count': 1, 
    #                               'wait_campaigns_count': 1, 
    #                             }, 
    #              ...
    #              ...
    #              ...
    #            },

                    
    #############################################################

    # 9. loop through each c widget in c_widgets_for_all_campaigns["data"] and
    # add its classification (white/grey/black) into c_widget["for_all_campaigns"]

    for c_widget in c_widgets_for_all_campaigns["data"].values():
        c_widget["for_all_campaigns"]["classification"] = classify_p_widget_for_all_campaigns(c_widget)

    # At this point in the process, c_widgets_for_all_campaigns looks like this
    # ("for_all_campaigns" has a "classification" key):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #              'mgid_start_date': '2018-08-09',
    #              'vol_end_date': '2019-02-05',
    #              'vol_start_date': '2018-08-09'},
    # {"data":   '6897s4532': { 'for_all_campaigns': { 'clicks': 8,
    #                                                  'classification': 'wait',
    #                                                  'cost': 0.16,
    #                                                  'global_status': 'not yet listed',
    #                                                  'leads': 0,
    #                                                  'referrer': [],
    #                                                  'revenue': 0.0,
    #                                                  'sales': 0,
    #                                                  'widget_id': '6897s4532'},
    #                           'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                           'good_campaigns_count': 1, 
    #                           'bad_campaigns_count': 1, 
    #                           'wait_campaigns_count': 1, 
    #                         }, 
    #              '123456s4235': { 'for_all_campaigns : {data...},
    #                               'for_each_campaign': [{campaign 1 data},{campaign 2 data}, ...]
    #                               'good_campaigns_count': 5, 
    #                               'bad_campaigns_count': 5, 
    #                               'wait_campaigns_count': 5, 
    #                             }, 
    #              ...
    #              ...
    #              ...
    #            },



    ##############################################################

    # 10. remove "for_each_campaign" "good_campaigns_count" "bad_campaigns_count" and 
    # "wait_campaigns_count" from each widget and add "good_campaigns_count" "bad_campaigns_count"
    # and "wait_campaigns_count" to c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]
    for c_widget in c_widgets_for_all_campaigns["data"]:
        c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["good_campaigns_count"] = c_widgets_for_all_campaigns["data"][c_widget]["good_campaigns_count"] 
        c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["bad_campaigns_count"] = c_widgets_for_all_campaigns["data"][c_widget]["bad_campaigns_count"] 
        c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]["wait_campaigns_count"] = c_widgets_for_all_campaigns["data"][c_widget]["wait_campaigns_count"] 
        c_widgets_for_all_campaigns["data"][c_widget] = c_widgets_for_all_campaigns["data"][c_widget]["for_all_campaigns"]

    # At this point in the process, p_widgets_for_all_campaigns looks like this
    # ("for_all_campaigns" has a "classification" key):
    # {'metadata': { 'mgid_end_date': '2019-02-04',
    #                'mgid_start_date': '2018-08-09',
    #                'vol_end_date': '2019-02-05',
    #                'vol_start_date': '2018-08-09'},
    # {"data":   '986897s4525':  { 'clicks': 8,
    #                             'classification': 'wait',
    #                             'cost': 0.16,
    #                             'global_status': 'not yet listed',
    #                             'leads': 0,
    #                             'referrer': [],
    #                             'revenue': 0.0,
    #                             'sales': 0,
    #                             'widget_id': '986897s4525',
    #                             'good_campaigns_count': 5, 
    #                             'bad_campaigns_count': 5, 
    #                             'wait_campaigns_count': 5,},
    #             '86123s452':  { 'clicks': 8,
    #                             'classification': 'wait',
    #                             'cost': 0.16,
    #                             'global_status': 'not yet listed',
    #                             'leads': 0,
    #                             'referrer': [],
    #                             'revenue': 0.0,
    #                             'sales': 0,
    #                             'widget_id': '86123s452',
    #                             'good_campaigns_count': 5, 
    #                             'bad_campaigns_count': 5, 
    #                             'wait_campaigns_count': 5, 
    #                           }, 
    #              ...
    #              ...
    #              ...
    #            },

    ############################################################
    # 11. Save p_widgets_for_all_campaigns to a json file and return it as a
    # json file 

    with open(f"../../data/c_widgets_for_all_campaigns/{date_range}_c_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(c_widgets_for_all_campaigns, file)

    return json.dumps(c_widgets_for_all_campaigns)




