from config.config import *
from functions.misc.send_email import send_email
from datetime import datetime
import requests
import sys

import pprint
pp=pprint.PrettyPrinter(indent=2)

def get_vol_countries_data(token, start_date, end_date):
    try:
        url = f"https://api.voluum.com/report?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=campaignName&direction=asc&columns=campaignName&columns=countryName&columns=campaignId&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=cpa&groupBy=campaign&groupBy=country-code&offset=0&limit=100000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token":
                token})
        res.raise_for_status()
        res = res.json()
        l = []
        for row in res["rows"]:
            print(row["campaignId"])
            print(row["countryName"])
            # if row["campaignId"] in l:
                # print("duplicate")
                # sys.exit()
            # else:
                # pp.pprint(row)
                # l.append(row["campaignId"])

        sys.exit()
    except requests.exceptions.RequestException as e:
            print("Failed - get_vol_countries_data()")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - get_vol_countries_data() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()
            

#############################
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range

token = get_vol_access_token(vol_access_id, vol_access_key)

dates = create_vol_date_range(180, mgid_timezone)
start_date = dates[0]
end_date = dates[1]

get_vol_countries_data(token, start_date, end_date)

