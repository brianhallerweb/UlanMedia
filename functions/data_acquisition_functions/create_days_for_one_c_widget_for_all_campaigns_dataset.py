from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
from datetime import datetime, timedelta
import requests
import json
import sys
import os
from functions.misc.send_email import send_email


def create_days_for_one_c_widget_for_all_campaigns_dataset(token, start_date, end_date, c_widget_id):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        
        days = {"metadata": {"vol_start_date": start_date, "vol_end_date":
            end_date}, "data": {}}

        while (end - start).days >= 30:
            temp_start = (end - timedelta(30)).strftime("%Y-%m-%d")
            temp_end = end.strftime("%Y-%m-%d")
            # print(f"request from {temp_start} to {temp_end}")

            url =f"https://api.voluum.com/report?from={temp_start}T00:00:00Z&to={temp_end}T00:00:00Z&tz=America%2FLos_Angeles&filter={c_widget_id}&conversionTimeMode=VISIT&sort=day&direction=desc&columns=day&columns=customVariable1&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=day&groupBy=custom-variable-1&offset=0&limit=1000000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"  
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
            end = datetime.strptime(temp_start, "%Y-%m-%d").date()
        if (end - start).days > 0:
            # print(f"request from {start} to {end}")
            url =f"https://api.voluum.com/report?from={start}T00:00:00Z&to={end}T00:00:00Z&tz=America%2FLos_Angeles&filter={c_widget_id}&conversionTimeMode=VISIT&sort=day&direction=desc&columns=day&columns=customVariable1&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cv&columns=roi&columns=epv&groupBy=day&groupBy=custom-variable-1&offset=0&limit=1000000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"  
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

        for campaign in conversions_for_each_campaign:
            for conversion in conversions_for_each_campaign[campaign]:
                widget_id = conversion["customVariable1"]
                if widget_id != c_widget_id:
                    continue
                day = conversion["visitTimestamp"].split(' ')[0] 
                conversion_type = conversion["transactionId"]
                if conversion_type == "account":
                    if day in days["data"]:
                        days["data"][day]["leads"] += 1
                elif conversion_type == "deposit":
                    if day in days["data"]:
                        days["data"][day]["sales"] += 1

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/days_for_one_c_widget_for_all_campaigns/{c_widget_id}_days_for_one_c_widget_for_all_campaigns_dataset.json", "w") as file:
            json.dump(days, file)

        return json.dumps(days)
    except:
        print("Failed - email sent")
        send_email("brianshaller@gmail.com", "Failed - create_days_for_one_c_widget_for_all_campaigns_dataset()", "Failed - create_days_for_one_c_widget_for_all_campaigns_dataset()")
        sys.exit()



