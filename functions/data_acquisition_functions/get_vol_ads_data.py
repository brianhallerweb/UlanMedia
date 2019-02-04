from config.config import *
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys

def get_vol_ads_data(token, start_date, end_date, timezone):
    try:
        # campaigns will be a list of dictionaries, where each dictionary is a
        # campaign with keys and values like {vol_id: "123", mgid_id: 123, ...}
        campaigns = get_campaign_sets()

        ads_data = {}
        for campaign in campaigns:
            vol_id = campaign["vol_id"]
            name = campaign["name"]
            url = f"https://api.voluum.com/report?from={start_date}T00%3A00%3A00Z&to={end_date}T00%3A00%3A00Z&tz={timezone}&sort=visits&direction=desc&columns=customVariable3&columns=visits&columns=conversions&columns=revenue&groupBy=custom-variable-3&offset=0&limit=100&include=ACTIVE&conversionTimeMode=VISIT&filter1=campaign&filter1Value={vol_id}"

            res = requests.get(url, headers = {"cwauth-token":
                    token})
            res.raise_for_status()
            res = res.json()
            # the response is a list of dictionaries. Each dictionary is an ad for the
            # campaign specified in the request. The ads_data dictionary will
            # have this structure: each key is an ad id (customvariable3) and each value is a dictionary
            # with stats for that ad 
            for ad in res["rows"]:
                ad_id = ad["customVariable3"]
                ads_data[ad_id] = {} 
                ads_data[ad_id]["ad_id"] = ad_id
                ads_data[ad_id]["vol_id"] = vol_id
                ads_data[ad_id]["name"] = name 
                ads_data[ad_id]["clicks"] = ad["visits"]
                ads_data[ad_id]["cost"] = ad["cost"]
                ads_data[ad_id]["conversions"] = ad["conversions"]
                ads_data[ad_id]["revenue"] = ad["revenue"]
        return ads_data
    except requests.exceptions.RequestException as e:
            print("Failed - get_vol_ads_data()")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - get_vol_ads_data() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()
  

