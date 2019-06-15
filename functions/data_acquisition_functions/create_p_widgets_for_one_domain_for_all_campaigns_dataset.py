from config.config import *
import json
import sys
import re
import os

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_p_widgets_for_one_domain_for_all_campaigns_dataset(date_range, domain):
    
    # 6/14 I'm not sure why I had this? But I think it is wrong
    # domains = domain.split(",")

    p_widgets_for_one_domain_for_all_campaigns = {"metadata": {"vol_start_date":
        "none", "vol_end_date":
        "none"}, "data": {}}

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
        complete_p_widgets = json.load(file)
    
    for p_widget in complete_p_widgets:
        if complete_p_widgets[p_widget]["for_all_campaigns"]["domain"] == domain:
            p_widgets_for_one_domain_for_all_campaigns["data"][p_widget] = complete_p_widgets[p_widget]["for_all_campaigns"]

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/p_widgets_for_one_domain_for_all_campaigns/{date_range}_{domain}_p_widgets_for_one_domain_for_all_campaigns_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_domain_for_all_campaigns, file)

    return json.dumps(p_widgets_for_one_domain_for_all_campaigns)


