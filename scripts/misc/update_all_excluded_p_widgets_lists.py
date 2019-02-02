from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign
import json
from functions.misc.get_campaign_sets import get_campaign_sets 

# use this script if you want to update all the excluded p widget lists.
# This script isn't ever called from the web app. 
# The only reason to use this is if you have included or excluded campaigns
# outside of the web app and would like to update the campaign "status" column
# on the web app. 
# In other words, the campaign "status" is updated whenever a campaign is
# excluded through the web app. If you exclude/include a campaign without using
# the web app, the campaign "status" column will be out of sync on the web app. 

campaigns = get_campaign_sets()

for campaign in campaigns:
    mgid_id = campaign["mgid_id"]
    excluded_p_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token,
            mgid_client_id, mgid_id)
    with open(f"../../excluded_p_widgets_lists/{mgid_id}_excluded_p_widgets.json", "w") as file:
        json.dump(excluded_p_widgets, file)
    print(f"{mgid_id} list created")

print("complete")

