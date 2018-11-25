import re
from datetime import datetime
import requests
import sys
from functions.misc.send_email import send_email

def get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, mgid_campaign_id):
    url=f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns/{mgid_campaign_id}?token={mgid_token}";
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        # the response is a dictionary of lists. The keys are widget ids.
        # The values are sources. If a widget id has a source, it must be 
        # this concatenation is necessary {widget_id}s{source_id}.
        # One strange thing about the response is that the source id appears
        # to be in a list but the [] are actually just part of the source id
        # string.
        excluded_widgets = []
        for key, value in response["widgetsFilterUid"]["widgets"].items():
            if value == "[]":
                excluded_widgets.append(key)
            else:
                value = re.sub(r'[\[\]]', "", value)
                excluded_widgets.append(f"{key}s{value}")
        # excluded_widgets is a list of excluded widget parent ids
        return excluded_widgets
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_excluded_widgets_by_campaign")
        send_email("brianshaller@gmail.com", "Failed - get_mgid_excluded_widgets_by_campaign() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

# explore what this function returns
# from config.config import *
# from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token

# mgid_token = get_mgid_access_token(mgid_login, mgid_password)
# data = get_mgid_excluded_widgets_by_campaign(mgid_token, mgid_client_id, "527383")
# print(data)
