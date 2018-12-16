import requests
from config.config import *
import json
import sys
import re
from datetime import datetime
from functions.misc.send_email import send_email

def create_offers_dataset(token, date_range, vol_start_date, vol_end_date):
    try:
        url = f"https://api.voluum.com/report?from={vol_start_date}T00%3A00%3A00Z&to={vol_end_date}T00%3A00%3A00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=offerName&direction=desc&columns=offerName&columns=campaignName&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=campaignId&columns=cpa&groupBy=offer&groupBy=campaign&offset=0&limit=100000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token": token})
        res.raise_for_status()
        if res.json()["totalRows"] != len(res.json()["rows"]):
            # you need to throw an error here
            print("problem")
            sys.exit()

        offers = {"metadata":{"vol_start_date": vol_start_date,
                              "vol_end_date": vol_end_date
                             },
                  "data": {}
                 }
        for row in res.json()["rows"]:
            campaignID = row["campaignId"]
            if campaignID not in offers["data"]:
                offers["data"][campaignID] = {}

        for row in res.json()["rows"]:
            campaignID = row["campaignId"] 
            offerID = row["offerId"]

            if row["offerName"].startswith("Global - 404"):
                offer_name = "404"
                offer_flow = "404"
            else:    
                pattern = re.compile(r'(^\w* - \w* - {1})(.[^(]*) (.*)')
                res = pattern.findall(row["offerName"])
                offer_string_parts = list(res[0])
                offer_name = offer_string_parts[1]
                offer_flow = offer_string_parts[2]

            if offer_flow == "(bin: unitedKingdom - English)":
                print(offer_name)
            
            if offerID not in offers["data"][campaignID]:
                offers["data"][campaignID][offerID] = {"clicks": row["visits"],
                                               "cost": row["cost"],
                                               "offerID": offerID,
                                               "campaignID": campaignID,
                                               "profit": row["profit"],
                                               "conversions": row["conversions"],
                                               "campaignName": row["campaignNamePostfix"],
                                               "offerName": offer_name,
                                               "offerFlow": offer_flow,
                                               }

        with open(f"../../data/offers/{date_range}_offers_dataset.json", "w") as file:
            json.dump(offers, file)

    except requests.exceptions.RequestException as e:
        print("Failed - get_vol_access_token()") 
        send_email("brianshaller@gmail.com", "Failed - get_vol_access_token() at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()


