from config.config import *
import json
import os
import sys

def create_countries_for_all_campaigns_dataset():

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_countries/oneeighty_complete_countries_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    countries_for_all_campaigns = {"metadata": metadata, "data": []}   
    for country_name in data:
        countries_for_all_campaigns["data"].append(data[country_name]["for_all_campaigns"])

    with open(f"../../data/countries_for_all_campaigns/oneeighty_countries_for_all_campaigns_dataset.json", "w") as file:
        json.dump(countries_for_all_campaigns, file)
    
    return json.dumps(countries_for_all_campaigns)


    









