from config.config import *
import sys
import json
import os

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_complete_countries_dataset():

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/countries/oneeighty_countries_dataset.json', 'r') as file:
        json_file = json.load(file)


    complete_countries = {"metadata": {"vol_start_date": json_file["metadata"]["vol_start_date"],
                                 "vol_end_date": json_file["metadata"]["vol_start_date"],
                                 },
                    "data": {}
                   }

    for country_name in json_file["data"]:
        for campaign_id in json_file["data"][country_name]:
            if country_name not in complete_countries["data"]:
                complete_countries["data"][country_name] = {
                        # 4/5/19 "for_all_campaigns" has the first campaign_id in it
                        # and it shouldn't have a campaign_id because its for
                        # all campaigns. Fix this later. 
                        "for_all_campaigns": json_file["data"][country_name][campaign_id],
                        "for_each_campaign": {}}
            else:
                complete_countries["data"][country_name]["for_all_campaigns"]["clicks"] += json_file["data"][country_name][campaign_id]["clicks"]
                complete_countries["data"][country_name]["for_all_campaigns"]["conversions"] += json_file["data"][country_name][campaign_id]["conversions"]
                complete_countries["data"][country_name]["for_all_campaigns"]["profit"] += json_file["data"][country_name][campaign_id]["profit"]
                complete_countries["data"][country_name]["for_all_campaigns"]["profit"] += json_file["data"][country_name][campaign_id]["profit"]
                complete_countries["data"][country_name]["for_all_campaigns"]["revenue"] += json_file["data"][country_name][campaign_id]["revenue"]

    for country_name in json_file["data"]:
        for campaign_id in json_file["data"][country_name]:
            complete_countries["data"][country_name]["for_each_campaign"][campaign_id] = json_file["data"][country_name][campaign_id]


    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/complete_countries/oneeighty_complete_countries_dataset.json", "w") as file:
        json.dump(complete_countries, file)




