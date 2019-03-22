from config.config import *
from functions.misc.send_email import send_email
from functions.misc.get_campaign_sets import get_campaign_sets
from datetime import datetime
import requests
import json
import sys
import re
import os

import pprint
pp=pprint.PrettyPrinter(indent=2)

# This is the "step 1" offers dataset that all other offers datasets are
# derived from. 

def create_offers_for_each_campaign_dataset(token, date_range, vol_start_date, vol_end_date):
    try:
        url = f"https://api.voluum.com/report?from={vol_start_date}T00%3A00%3A00Z&to={vol_end_date}T00%3A00%3A00Z&tz=America%2FLos_Angeles&conversionTimeMode=VISIT&sort=offerName&direction=desc&columns=offerName&columns=campaignName&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=campaignId&columns=cpa&groupBy=offer&groupBy=campaign&offset=0&limit=100000&include=ACTIVE&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc"
        res = requests.get(url, headers = {"cwauth-token": token})
        res.raise_for_status()
        if res.json()["totalRows"] != len(res.json()["rows"]):
            # you need to throw an error here
            print("problem")
            sys.exit()
        
        ############################3
        # create an offer weight lookup dictionary
        weight_url = f"https://api.voluum.com/flow/{vol_flow_id}"
        weight_res = requests.get(weight_url, headers = {"cwauth-token": token})
        weight_res.raise_for_status()
        weight_res = weight_res.json()
        weight_lookup = {}
        for path_group in weight_res["conditionalPathsGroups"]:
            for offer in path_group["paths"][0]["offers"]:
                offer_id = offer["offer"]["id"]
                if offer_id not in weight_lookup:
                    weight_lookup[offer_id] = offer["weight"]
                else:
                    print("there shouldn't be any repeats")
        #########################

        offers = {"metadata":{"vol_start_date": vol_start_date,
                              "vol_end_date": vol_end_date
                             },
                  "data": {}
                 }

        for row in res.json()["rows"]:
            campaign_id = row["campaignId"]
            if campaign_id not in offers["data"]:
                offers["data"][campaign_id] = {}

        campaigns = get_campaign_sets()
        campaign_ids = []
        for campaign in campaigns:
            campaign_ids.append(campaign["vol_id"])

        for row in res.json()["rows"]:
            campaign_id = row["campaignId"] 
            offer_id = row["offerId"]

            if (campaign_id not in campaign_ids) | (row["offerName"].startswith("Global - 404")):
                continue
            else:    
                pattern = re.compile(r'(^\w* - \w* - {1})(.[^(]*) (.*)')
                res = pattern.findall(row["offerName"])
                offer_string_parts = list(res[0])
                c_offer_name = offer_string_parts[1]
                flow_rule = offer_string_parts[2]

                ##############################
                # find parent_offer_name
                country_list = ["spain", "latam", "brazil", "portugal"]
                tier_list = ["tier1", "tier3"]
                offer_words = c_offer_name.split(" ")
                # remove the country code at the end (eg. DE)
                offer_words.pop()
                # remove the country name if there is one (eg. spain)
                if offer_words[len(offer_words) - 1] in country_list:
                    offer_words.pop()
                # remove the tier if there is one (eg. tier1)
                if offer_words[len(offer_words) - 1] in tier_list:
                    offer_words.pop()
                p_offer_name = " ".join(offer_words)

                # why is this happening
                # maybe some offers are taking the default weighting?
                # they don't seem to have a weighting 
                if offer_id not in weight_lookup:
                    vol_weight = "NA"
                else:
                    vol_weight = weight_lookup[offer_id]


            if offer_id not in offers["data"][campaign_id]:
                offers["data"][campaign_id][offer_id] = {"clicks": row["visits"],
                                               "cost": row["cost"],
                                               "offer_id": offer_id,
                                               "profit": row["profit"],
                                               "revenue": row["profit"] + row["cost"],
                                               "conversions": row["conversions"],
                                               "offer_id": offer_id,
                                               "campaign_id": campaign_id,
                                               "vol_offer_name": row["offerName"],
                                               "offer_name": f"{c_offer_name} {flow_rule}",
                                               "p_offer_name": p_offer_name,
                                               "c_offer_name": c_offer_name,
                                               "flow_rule": flow_rule,
                                               "vol_weight": vol_weight
                                               }

        with open(f"{os.environ.get('ULANMEDIAAPP')}/data/offers_for_each_campaign/{date_range}_offers_for_each_campaign_dataset.json", "w") as file:
            json.dump(offers, file)

    except requests.exceptions.RequestException as e:
        print("Failed - create_offers_for_each_campaign_dataset()") 
        send_email("brianshaller@gmail.com", "Failed - create_offers_for_each_campaign_dataset() at " +
                str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()


