from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
import json
import sys
import os

def create_campaigns_for_one_country_dataset(country_name):

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_countries/oneeighty_complete_countries_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    campaigns_for_one_country = {"metadata": metadata, "data": data[country_name]["for_each_campaign"]}   

    campaigns_sets = get_campaign_sets()
    campaigns_lookup = {}
    for campaign in campaigns_sets:
        campaigns_lookup[campaign["vol_id"]] = campaign["name"]

    for campaign_id in campaigns_for_one_country["data"]:
        if campaign_id not in campaigns_lookup:
            # 4/6/19 why is this happening? A campaign id coming back from
            # voluum ins't in campaign sets?
            campaigns_for_one_country["data"][campaign_id]["campaign_name"] = "NaN"
        else:
            campaigns_for_one_country["data"][campaign_id]["campaign_name"] = campaigns_lookup[campaign_id]

    with open(f"../../data/campaigns_for_one_country/{country_name}_campaigns_for_one_country_dataset.json", "w") as file:
        json.dump(campaigns_for_one_country, file)

    return json.dumps(campaigns_for_one_country)


    









