from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
import json
from functions.misc.get_campaign_sets import get_campaign_sets 


mgid_token = get_mgid_access_token(mgid_login, mgid_password)


campaigns = get_campaign_sets()

for campaign in campaigns:
    mgid_id = campaign["mgid_id"]
    excluded_p_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token,
            mgid_client_id, mgid_id)
    with open(f"../../excluded_p_widgets_lists/{mgid_id}_excluded_p_widgets.json", "w") as file:
        json.dump(excluded_p_widgets, file)
    print(f"{mgid_id} list created")

print("complete")

