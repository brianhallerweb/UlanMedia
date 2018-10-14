from config.config import *
from functions.data_acquisition_functions.get_all_campaigns_daily_stats import get_all_campaigns_daily_stats
import json

def create_days_for_one_campaign_dataset(vol_token, mgid_token, start_date, end_date, output_name):
    # get daily stats by campaign by day  
    daily_stats = get_all_campaigns_daily_stats(vol_token,
                                                       mgidVolTrafficSourceId
                                                       , start_date, end_date)

    with open(f"../../data/days_for_one_campaign/{output_name}.json", "w") as file:
        json.dump(daily_stats, file)

    print(f"{output_name} created")


