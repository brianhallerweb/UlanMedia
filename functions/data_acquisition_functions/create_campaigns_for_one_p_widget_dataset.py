from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.get_whitelist import get_whitelist
from functions.misc.get_greylist import get_greylist
from functions.misc.get_blacklist import get_blacklist
import json
import os
import sys
import re
from functions.misc.send_email import send_email


def create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range,
        max_rec_bid):
    try:

        ########################################################

        # 1. get some prerequisite data

        max_rec_bid = float(max_rec_bid)

        campaigns = get_campaign_sets()
        widget_whitelist = get_whitelist()
        widget_greylist = get_greylist()
        widget_blacklist = get_blacklist()

        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
            complete_p_widgets = json.load(file)

        if complete_p_widgets.get(p_widget_id):
            complete_p_widget = complete_p_widgets[p_widget_id]
        else:
            complete_p_widget = {"for_all_campaigns":{"domain": "unknown"}, "for_each_campaign":[]}


        ########################################################

        # 2. set up the basic data structure you want to create

        campaigns_for_one_p_widget = {"metadata":{}, "data":[]} 

        #########################################################

        # 3. Add the metadata. 

        vol_id_for_adding_metadata = campaigns[0]["vol_id"]
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/p_and_c_widgets_for_one_campaign/{campaigns[0]["vol_id"]}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)
        campaigns_for_one_p_widget["metadata"]["mgid_start_date"] = json_file["metadata"]["mgid_start_date"]
        campaigns_for_one_p_widget["metadata"]["mgid_end_date"] = json_file["metadata"]["mgid_end_date"] 
        campaigns_for_one_p_widget["metadata"]["vol_start_date"] = json_file["metadata"]["vol_start_date"]
        campaigns_for_one_p_widget["metadata"]["vol_end_date"] = json_file["metadata"]["vol_end_date"]
        if complete_p_widgets.get(p_widget_id):
            campaigns_for_one_p_widget["metadata"]["p_widget_classification"] = complete_p_widget["for_all_campaigns"]["classification"]
            campaigns_for_one_p_widget["metadata"]["p_widget_global_status"] = complete_p_widget["for_all_campaigns"]["global_status"]
            campaigns_for_one_p_widget["metadata"]["p_widget_has_children"] = complete_p_widget["for_all_campaigns"]["has_children"]
            campaigns_for_one_p_widget["metadata"]["p_widget_has_mismatch_classification_and_global_status"] = complete_p_widget["for_all_campaigns"]["has_mismatch_classification_and_global_status"]
            campaigns_for_one_p_widget["metadata"]["good_campaigns_count"] = complete_p_widget["good_campaigns_count"]
            campaigns_for_one_p_widget["metadata"]["bad_campaigns_count"] = complete_p_widget["bad_campaigns_count"]
            campaigns_for_one_p_widget["metadata"]["wait_campaigns_count"] = complete_p_widget["wait_campaigns_count"]

        #########################################################

        # 4. Add the data

        campaigns_for_one_p_widget["data"] = complete_p_widget["for_each_campaign"]

        for campaign in campaigns_for_one_p_widget["data"]:
            campaign["domain"] = complete_p_widget["for_all_campaigns"]["domain"]

        for campaign in campaigns_for_one_p_widget["data"]:
            sales = campaign["sales"]
            mpl = campaign["mpl"]
            if campaign["leads"] > 0:
                cpl = campaign["cost"]/campaign["leads"]
            if campaign["clicks"] > 0:
                epc = campaign["revenue"]/campaign["clicks"]
            c_bid = campaign["c_bid"]
            w_bid = campaign["w_bid"]
            coeff = campaign["coeff"]

            if sales > 0:
                campaign["rec_w_bid"] = epc - epc * .3
            elif campaign["leads"] > 0:
                if cpl == 0:
                    campaign["rec_w_bid"] = c_bid
                else:
                    campaign["rec_w_bid"] = c_bid * mpl / cpl / 2
            else:
                campaign["rec_w_bid"] = c_bid

            if campaign["rec_w_bid"] > max_rec_bid:
                campaign["rec_w_bid"] = max_rec_bid

            campaign["rec_coeff"] = campaign["rec_w_bid"] / c_bid

            rec_w_bid = campaign["rec_w_bid"]
            rec_coeff = campaign["rec_coeff"]

            if w_bid != rec_w_bid:
                campaign["mismatch_w_bid_and_rec_w_bid"] = True
            else:
                campaign["mismatch_w_bid_and_rec_w_bid"] = False

            if coeff != rec_coeff:
                campaign["mismatch_coeff_and_rec_coeff"] = True
            else:
                campaign["mismatch_coeff_and_rec_coeff"] = False


        ############################################################
        # 11. Save campaigns_for_one_p_widget to a json file and return it as a
        # json file 

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/campaigns_for_one_p_widget/{p_widget_id}_{date_range}_campaigns_for_one_p_widget_dataset.json", "w") as file:
            json.dump(campaigns_for_one_p_widget, file)

        return json.dumps(campaigns_for_one_p_widget)
    except:
        print("Failed - email sent")
        send_email("brianshaller@gmail.com", "Failed - create_campaigns_for_one_p_widget_dataset()", "Failed - create_campaigns_for_one_p_widget_dataset()")
        sys.exit()

