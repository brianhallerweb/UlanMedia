from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
from datetime import datetime, timedelta
import requests
import json
import sys
import re
import os
# import pprint
# pp=pprint.PrettyPrinter(indent=2)



def create_days_for_one_p_widget_for_one_campaign_dataset(token, start_date, end_date, p_widget_id, campaign_id):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    days = {"metadata": {"vol_start_date": start_date, "vol_end_date":
        end_date}, "data": {}}

    url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&filter={p_widget_id}&conversionTimeMode=VISIT&sort=day&direction=desc&columns=day&columns=customVariable1&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=day&groupBy=custom-variable-1&offset=0&limit=1000000&include=ACTIVE&filter1=campaign&filter1Value={campaign_id}"
    res = requests.get(url, headers = {"cwauth-token": token}).json()
    for row in res["rows"]:
        day = row["day"]
        clicks = row["visits"]
        cost = row["cost"]
        revenue = row["revenue"]
        profit = row["profit"]
        if day in days["data"]:
            days["data"][day]["clicks"] += clicks
            days["data"][day]["cost"] += cost
            days["data"][day]["revenue"] += revenue 
            days["data"][day]["profit"] += profit
        else:
            days["data"][day] = {"clicks": clicks,
                    "cost": cost, 
                    "revenue": revenue, 
                    "profit": profit, 
                    "leads": 0,
                    "sales": 0,
                    "day": day
                    }


    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/conversions_for_each_campaign/oneeighty_conversions_for_each_campaign_dataset.json', 'r') as file:
        json_file = json.load(file)
    conversions_for_each_campaign = json_file["data"]

    p_widget_id_pattern = re.compile(r'(\d*)(s*)(\d*)')

    if campaign_id in conversions_for_each_campaign:

        for conversion in conversions_for_each_campaign[campaign_id]:
            widget_id = list(p_widget_id_pattern.findall(conversion["customVariable1"])[0])[0]
            if widget_id != p_widget_id:
                continue
            day = conversion["visitTimestamp"].split(' ')[0] 
            conversion_type = conversion["transactionId"]
            if conversion_type == "account":
                if day in days["data"]:
                    days["data"][day]["leads"] += 1
            elif conversion_type == "deposit":
                if day in days["data"]:
                    days["data"][day]["sales"] += 1

    with open(f"{os.environ.get('ULANMEDIAAPP')}/data/days_for_one_p_widget_for_one_campaign/{p_widget_id}_{campaign_id}_days_for_one_p_widget_for_one_campaign_dataset.json", "w") as file:
        json.dump(days, file)

    return json.dumps(days)

#10/13/19 troubleshooting
# from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
# from config.config import *
# from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
# from functions.misc.create_vol_date_range import create_vol_date_range

# token = get_vol_access_token(vol_access_id, vol_access_key)
# vol_dates = create_vol_date_range(180, mgid_timezone)
# vol_start_date = vol_dates[0]
# vol_end_date = vol_dates[1]


# create_days_for_one_p_widget_for_one_campaign_dataset(token, vol_start_date, vol_end_date, '5763306', '500d6941-a19a-4a79-9bcb-251759a473ea')
