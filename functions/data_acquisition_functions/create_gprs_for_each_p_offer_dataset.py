from config.config import *
from datetime import datetime
import json
import sys
import re
import os
from functions.classification_functions.classify_offer_for_all_campaigns import classify_offer_for_all_campaigns

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_gprs_for_each_p_offer_dataset(date_range):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/offers_for_each_flow_rule/{date_range}_offers_for_each_flow_rule_dataset.json', 'r') as file:
        json_file = json.load(file)
    offers_for_each_flow_rule = json_file["data"]

    #####################################

    gprs_for_each_p_offer = {}   

    for flow_rule in offers_for_each_flow_rule:
        for offer in offers_for_each_flow_rule[flow_rule]:
            p_offer_name = offers_for_each_flow_rule[flow_rule][offer]["p_offer_name"]
            gpr = offers_for_each_flow_rule[flow_rule][offer]["gpr"]
            gprs_for_each_p_offer[p_offer_name] = {"name": p_offer_name, "gpr":
                    gpr}

    gprs_for_each_p_offer_list = []
    for p_offer_name in gprs_for_each_p_offer:
        gprs_for_each_p_offer_list.append(gprs_for_each_p_offer[p_offer_name])
    
    return json.dumps(gprs_for_each_p_offer_list)

