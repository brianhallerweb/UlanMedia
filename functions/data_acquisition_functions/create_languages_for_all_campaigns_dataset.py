from config.config import *
import json
import os
import sys
from functions.misc.send_email import send_email


def create_languages_for_all_campaigns_dataset(date_range):
    try:
        with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_languages/{date_range}_complete_languages_dataset.json', 'r') as file:
            json_file = json.load(file)

        metadata = json_file["metadata"]
        data = json_file["data"]

        languages_for_all_campaigns = {"metadata": metadata, "data": []}   
        for language_name in data:
            languages_for_all_campaigns["data"].append(data[language_name]["for_all_campaigns"])

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/languages_for_all_campaigns/{date_range}_languages_for_all_campaigns_dataset.json", "w") as file:
            json.dump(languages_for_all_campaigns, file)
        
        return json.dumps(languages_for_all_campaigns)
    except:
        print("Failed - email sent")
        send_email("brianshaller@gmail.com", "Failed - create_languages_for_all_campaigns_dataset()", "Failed - create_languages_for_all_campaigns_dataset()")
        sys.exit()



    









