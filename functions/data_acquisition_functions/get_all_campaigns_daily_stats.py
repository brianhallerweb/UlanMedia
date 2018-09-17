import requests
import re
from datetime import datetime
import sys
import json
from functions.misc.send_email import send_email

def get_all_campaigns_daily_stats(token,
        traffic_source_id, start_date, end_date):
    url = f"https://api.voluum.com/report?from={start_date}T00%3A00%3A00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&sort=campaignName&direction=desc&columns=campaignName&columns=day&columns=campaignId&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=cpv&groupBy=campaign&groupBy=day&offset=0&limit=1000000&include=ACTIVE&conversionTimeMode=VISIT&filter1=traffic-source&filter1Value={traffic_source_id}";
    try:
        campaigns = requests.get(url, headers = {"cwauth-token": token}).json()
        #the data that returns is a list of dictionaries. Each dictionary is a
        #campaign for 1 day of the time period queried. You want to organize
        #the data into a dictionary of campaigns, with each campaign being a
        #list of dictionaries representing eachday of the time period queried. 
        if campaigns["totalRows"] != len(campaigns["rows"]):
            # The get request has a limit of 1,000,000 so if there are more than 
            # 1,000,000 conversions returned, this exception will be raised. 
            raise Exception("voluum didn't return all the conversion data.")
        print("all campaign data returned from voluum")
        
        campaigns_data = {} 
        for campaign in campaigns["rows"]:
            campaign_id = campaign["campaignId"]
            campaign_name = re.sub(r"^.* - ", "",campaign["campaignName"], count=1)        
            if campaign_id not in campaigns_data:
                campaigns_data[campaign_id] = [{"vol_id": campaign_id, "name": campaign_name,
                    "visits": campaign["visits"], "conversions":
                    campaign["conversions"], "cost": campaign["cost"], "revenue": campaign["revenue"], "day": campaign["day"]}]
            elif campaign_id in campaigns_data:
                campaigns_data[campaign_id].append({"vol_id": campaign_id, "name": campaign_name,
                    "visits": campaign["visits"], "conversions":
                    campaign["conversions"], "cost": campaign["cost"], "revenue": campaign["revenue"], "day": campaign["day"]})
            
        return campaigns_data 
    except requests.exceptions.RequestException as e:
        print("Failed - get_all_campaigns_daily_stats()") 
        send_email("brianshaller@gmail.com", "Failed - get_all_campaigns_daily_stats at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

