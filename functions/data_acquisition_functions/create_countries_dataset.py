from config.config import *
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys
import json
import os

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_countries_dataset(token, start_date, end_date):
    try:
        url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=campaignName&direction=asc&columns=campaignName&columns=countryName&columns=campaignId&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=cpa&groupBy=campaign&groupBy=country-code&offset=0&limit=100000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token":
                token})
        res.raise_for_status()
        res = res.json()
        countries = {"metadata": {"vol_start_date": start_date,
                                 "vol_end_date": end_date
                                 },
                    "data": {}}
        for row in res["rows"]:
            country_name = row["countryName"]
            campaign_id = row["campaignId"]
            if country_name not in countries["data"]:
                countries["data"][country_name] = {campaign_id: {
                    "campaign_id": campaign_id,
                    "country_name": country_name,
                    "clicks": row["clicks"],
                    "conversions": row["conversions"],
                    "cost": row["cost"],
                    # what is the difference between clicks, impressions,
                    # visits?
                    "impressions": row["impressions"],
                    "visits": row["visits"],
                    "profit": row["profit"],
                    "revenue": row["revenue"]
                    }}
            else:
                countries["data"][country_name][campaign_id] = {
                    "campaign_id": campaign_id,
                    "country_name": country_name,
                    "clicks": row["clicks"],
                    "conversions": row["conversions"],
                    "cost": row["cost"],
                    "impressions": row["impressions"],
                    "visits": row["visits"],
                    "profit": row["profit"],
                    "revenue": row["revenue"]
                    }

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/countries/oneeighty_countries_dataset.json", "w") as file:
            json.dump(countries, file)

    except requests.exceptions.RequestException as e:
            print("Failed - create_countries_dataset()")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - create_countries_dataset() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()
            

