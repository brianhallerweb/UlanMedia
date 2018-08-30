import requests
import re
from datetime import datetime
import sys
import json
from functions.misc.send_email import send_email

def get_all_campaign_conversions_by_traffic_source(token,
        traffic_source_id, start_date, end_date):
    #the end_date isn't used in the url because I always want conversions
    #the start date and today. The end date is only used to filter out clicks
    #(visitTimestamp) between start_date and end_date.
    today = datetime.now().strftime("%Y-%m-%d")
    url=f"https://api.voluum.com/report/conversions?from={start_date}T00%3A00%3A00Z&to={today}T00:00:00Z&tz=America%2FLos_Angeles&filter={traffic_source_id}&sort=campaignName&direction=asc&columns=transactionId&columns=revenue&columns=campaignName&columns=trafficSourceId&groupBy=conversion&offset=0&limit=100000&include=ACTIVE&conversionTimeMode=VISIT"
    try:
        campaigns = requests.get(url, headers = {"cwauth-token": token}).json()
        if campaigns["totalRows"] != len(campaigns["rows"]):
            # The get request has a limit of 100,000 so if there are more than 
            # 100,000 conversions returned, this exception will be raised. 
            raise Exception("voluum didn't return all the conversion data.")
        print("all campaign data returned from voluum")
        campaigns_data = {} 
        for campaign in campaigns["rows"]:
            campaign_name = re.sub(r"^.* - ", "",campaign["campaignName"], count=1)        
            if campaign_name not in campaigns_data:
                campaigns_data[campaign_name] = {"name": campaign_name, "revenue": 0,
                        "leads": 0, "sales": 0}
        for campaign in campaigns["rows"]:
            visit_date = re.sub(r"[\s].*", "", campaign["visitTimestamp"])
            visit_date = datetime.strptime(visit_date, "%Y-%m-%d").date()
            start_date = datetime.strptime(str(start_date), "%Y-%m-%d").date()
            end_date = datetime.strptime(str(end_date), "%Y-%m-%d").date()
            # This conditional is necessary because the api returns conversions
            # between start_date and end_date, and I want conversions for
            # clicks that occurred between start_date and end_date.
            if visit_date >= start_date and visit_date <= end_date:
                revenue = campaign["revenue"]
                campaign_name = re.sub(r"^.* - ", "",campaign["campaignName"], count=1)        
                lead = 0
                sale = 0
                if campaign["transactionId"] == "account":
                    lead = 1
                elif campaign["transactionId"] == "deposit":
                    sale = 1
                campaigns_data[campaign_name]["leads"] += lead
                campaigns_data[campaign_name]["sales"] += sale
                campaigns_data[campaign_name]["revenue"] += revenue 
        return campaigns_data 
    except requests.exceptions.RequestException as e:
        print("Failed - get_all_campaign_conversions_by_traffic_source()") 
        send_email("brianshaller@gmail.com", "Failed - get_all_campaign_conversions_by_traffic_source at " +
                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()

