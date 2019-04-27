from config.config import *
from config.mgid_token import mgid_token
from functions.misc.get_and_return_new_mgid_token import get_and_return_new_mgid_token
import requests

def get_mgid_included_widgets_by_campaign(token, campaign_id, start_date, end_date):
    url =f"https://api.mgid.com/v1/goodhits/campaigns/{campaign_id}/quality-analysis?token={token}&campaignId={campaign_id}&dateInterval=interval&startDate={start_date}&endDate={end_date}";
    response = requests.get(url) 
    if response.status_code == 401:
        mgid_token = get_and_return_new_mgid_token()
        return get_mgid_widget_clicks_and_costs_by_campaign(mgid_token, campaign_id, start_date, end_date)

    response.raise_for_status()
    response = response.json()
    included_widgets = []
    if response[campaign_id][start_date + "_" + end_date] == []:
        return included_widgets
    for id, data in response[campaign_id][start_date + "_" + end_date].items():
        widget_id = id
        if data["sources"]:
            for source_id, source_data in data["sources"].items():
                if source_id is not "0":
                    widget_id = f"{id}s{source_id}"
                included_widgets.append(widget_id)
        else: 
            included_widgets.append(widget_id)
    return included_widgets

