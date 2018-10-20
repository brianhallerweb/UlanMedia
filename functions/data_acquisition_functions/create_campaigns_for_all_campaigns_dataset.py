from config.config import *
from functions.data_acquisition_functions.get_all_campaign_conversions_by_traffic_source import get_all_campaign_conversions_by_traffic_source
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.misc.create_mgid_date_range import create_mgid_date_range
import json

def create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago, output_name):
    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    mgid_dates = create_mgid_date_range(days_ago, mgid_timezone)
    mgid_start_date = mgid_dates[0]
    mgid_end_date = mgid_dates[1]

    # get leads, sales, and revenue by campaign from voluum 
    vol_campaign_data = get_all_campaign_conversions_by_traffic_source(vol_token,
                                                       mgidVolTrafficSourceId
                                                       , vol_start_date, vol_end_date)
    # get clicks, imps, and cost by campaign from mgid
    mgid_campaign_data = get_mgid_campaign_costs(mgid_token, mgid_client_id,
                                              mgid_start_date,
                                              mgid_end_date)["campaigns-stat"]

    # get a new version of the campaign_sets text file that Mike regularly edits
    campaign_sets = get_campaign_sets() 

    # create an array of dicts where each dict is a campaign
    # the stats in each campaign come from both mgid and voluum
    # the campaign data is only collected for campains in campaign_sets.txt
    campaigns_data = []
    for row in campaign_sets:
        mgid_campaign_id = str(row["mgid_id"])
        vol_campaign_id = str(row["vol_id"])
        campaign_name = str(row["name"])
        max_lead_cpa = str(row["max_lead_cpa"])
        max_sale_cpa = str(row["max_sale_cpa"])
        campaign_data = {}
        campaign_data["mgid_id"] = mgid_campaign_id
        campaign_data["vol_id"] = vol_campaign_id
        campaign_data["name"] = campaign_name
        campaign_data["max_lead_cpa"] = max_lead_cpa
        campaign_data["max_sale_cpa"] = max_sale_cpa
        campaign_data["clicks"] = mgid_campaign_data[mgid_campaign_id]["clicks"]
        campaign_data["imps"] = mgid_campaign_data[mgid_campaign_id]["imps"]
        campaign_data["cost"] = mgid_campaign_data[mgid_campaign_id]["spent"]
        if vol_campaign_id in vol_campaign_data:
            campaign_data["leads"] = vol_campaign_data[vol_campaign_id]["leads"]
            campaign_data["sales"] = vol_campaign_data[vol_campaign_id]["sales"]
            campaign_data["revenue"] = vol_campaign_data[vol_campaign_id]["revenue"]
        else:
            campaign_data["leads"] = 0
            campaign_data["sales"] = 0
            campaign_data["revenue"] = 0
        campaigns_data.append(campaign_data)


    with open(f"../../data/campaigns_for_all_campaigns/{output_name}.json", "w") as file:
        json.dump(campaigns_data, file)

    print(f"{output_name} created")

