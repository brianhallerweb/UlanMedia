from config.config import *
import json
import sys
import re
import os

import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_widgets_for_one_domain_for_all_campaigns_dataset(date_range, domain):
    
    domains = domain.split(",")

    widgets_for_one_domain_for_all_campaigns = {"metadata": {"vol_start_date":
        "test", "vol_end_date":
        "test"}, "data": {}}

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)
    
    for p_widget in complete_p_widgets:
        if complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] in domains:
            widgets_for_one_domain_for_all_campaigns["data"][p_widget] = complete_p_widgets[p_widget]["for_all_campaigns"]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_c_widgets/{date_range}_complete_c_widgets_dataset.json', 'r') as file:
        complete_c_widgets = json.load(file)
    
    for c_widget in complete_c_widgets:
        if complete_c_widgets[c_widget]["for_all_campaigns"]["domain"] in domains:
            widgets_for_one_domain_for_all_campaigns["data"][c_widget] = complete_c_widgets[c_widget]["for_all_campaigns"]


    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/widgets_for_one_domain_for_all_campaigns/{date_range}_{domain}_widgets_for_one_domain_for_all_campaigns_dataset.json", "w") as file:
        json.dump(widgets_for_one_domain_for_all_campaigns, file)

    return json.dumps(widgets_for_one_domain_for_all_campaigns)


