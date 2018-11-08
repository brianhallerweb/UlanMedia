from config.config import *
from functions.data_acquisition_functions.get_all_campaigns_daily_stats import get_all_campaigns_daily_stats
from functions.misc.create_vol_date_range import create_vol_date_range
import json

def create_days_for_one_campaign_dataset(vol_token, mgid_token, days_ago, output_name):
    vol_date_range = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_date_range[0]
    vol_end_date = vol_date_range[1]
    print(f"vol start date: {vol_start_date}")
    print(f"vol end date: {vol_end_date}")

    #mgid_token is not used yet

    # get daily stats by campaign by day  
    daily_stats = get_all_campaigns_daily_stats(vol_token,
                                                       mgidVolTrafficSourceId
                                                       , vol_start_date, vol_end_date)

    with open(f"../../data/days_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(daily_stats, file)

    print(f"{output_name} created")


