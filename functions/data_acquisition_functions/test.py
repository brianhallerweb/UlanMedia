from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
import requests
import json
import sys
import re
import os

import pprint
pp=pprint.PrettyPrinter(indent=2)

def test(token):
    vol_weight_url = f"https://api.voluum.com/flow/{vol_flow_id}"
    vol_weight_res = requests.get(vol_weight_url, headers = {"cwauth-token": token})
    vol_weight_res.raise_for_status()
    vol_weight_res = vol_weight_res.json()
    vol_index_lookup = {}
    # for offer in vol_weight_res["defaultPaths"][0]["offers"]:
        # offer_id = offer["offer"]["id"]
        # if offer_id not in vol_weight_lookup:
            # vol_weight_lookup[offer_id] = offer["weight"]
        # else:
            # print("there shouldn't be any repeats")
    # for path_group in vol_weight_res["conditionalPathsGroups"]:
        # for offer in path_group["paths"][0]["offers"]:
            # offer_id = offer["offer"]["id"]
            # if offer_id not in vol_weight_lookup:
                # vol_weight_lookup[offer_id] = offer["weight"]
            # else:
                # print("there shouldn't be any repeats")
    # the 2 keys that matter at conditionalPathsGroups and defaultPaths
    index = 1
    for flow_rule in vol_weight_res["conditionalPathsGroups"]:
        vol_index_lookup[flow_rule["name"]] = index
        index += 1
    for flow_rule in vol_weight_res["defaultPaths"]:
        vol_index_lookup[flow_rule["name"]] = index
        index += 1
    for key in vol_index_lookup:
        print(key)


vol_token = get_vol_access_token(vol_access_id, vol_access_key)
test(vol_token)
