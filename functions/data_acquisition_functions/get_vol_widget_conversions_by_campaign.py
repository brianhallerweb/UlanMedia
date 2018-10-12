import requests
import re
from datetime import datetime
from functions.misc.send_email import send_email
import sys

def get_vol_widget_conversions_by_campaign(token, campaign_id, start_date,
        end_date):
    try:
        url =f"https://api.voluum.com/report/conversions?from={start_date}T00%3A00%3A00Z&to={end_date}T00%3A00%3A00Z&tz=America%2FLos_Angeles&sort=customVariable1&direction=asc&columns=transactionId&columns=customVariable1&groupBy=conversion&offset=0&limit=100000&include=ACTIVE&conversionTimeMode=VISIT&filter1=campaign&filter1Value={campaign_id}"
        response = requests.get(url, headers = {"cwauth-token": token})
        response.raise_for_status()
        # All the logic below takes each conversion in the response and accumulates
        # them into widgets_data, which is a dictionary of widgets. So the end
        # result is a dictionary of accumulated conversion data for each widget for
        # the chosen period of time.
        if response.json()["rows"] == []:
            return {} 
        response = response.json()["rows"]
        widgets_data = {}
        domain_pattern = re.compile("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)")
        for conversion in response:
            widget_id = conversion["customVariable1"]
            revenue = conversion["revenue"]
            referrer = domain_pattern.findall(conversion["referrerDomain"])
            if referrer != []:
                referrer = referrer[0]
            lead = 0
            sale = 0
            if conversion["transactionId"] == "account":
                lead = 1
            elif conversion["transactionId"] == "deposit":
                sale = 1
            if widget_id not in widgets_data:
                widgets_data[widget_id] = {"widget_id": widget_id, "revenue":
                        revenue, "leads": lead, "sales": sale, "referrer": []}
                if referrer != []:
                    widgets_data[widget_id]["referrer"].append(referrer)
            elif widget_id in widgets_data:
                widgets_data[widget_id] = {"widget_id": widget_id, "revenue":
                        widgets_data[widget_id]["revenue"] + revenue, "leads":
                        widgets_data[widget_id]["leads"] + lead, "sales":
                        widgets_data[widget_id]["sales"] + sale, "referrer":
                        widgets_data[widget_id]["referrer"]} 
                if referrer not in widgets_data[widget_id]["referrer"] and referrer != []:
                    widgets_data[widget_id]["referrer"].append(referrer)
        return widgets_data 
    except requests.exceptions.RequestException as e:
        print("Failed - get_vol_widget_conversions_by_campaign")
        send_email("brianshaller@gmail.com", "Failed - get_vol_widget_conversions_by_campaign() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
