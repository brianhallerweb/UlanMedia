from config.config import *
import json
import os
import sys

def create_languages_for_all_campaigns_dataset():

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_languages/oneeighty_complete_languages_dataset.json', 'r') as file:
        json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]

    languages_for_all_campaigns = {"metadata": metadata, "data": []}   
    for language_name in data:
        languages_for_all_campaigns["data"].append(data[language_name]["for_all_campaigns"])

    with open(f"../../data/languages_for_all_campaigns/oneeighty_languages_for_all_campaigns_dataset.json", "w") as file:
        json.dump(languages_for_all_campaigns, file)
    
    return json.dumps(languages_for_all_campaigns)


    









