from config.config import *
from functions.data_acquisition_functions.get_all_campaigns_daily_stats import get_all_campaigns_daily_stats
import json

def create_by_campaigns_by_days_data_set(vol_token, mgid_token, start_date, end_date, output_name):
    # get daily stats by campaign by day  
    by_campaign_by_day_daily_stats = get_all_campaigns_daily_stats(vol_token,
                                                       mgidVolTrafficSourceId
                                                       , start_date, end_date)

    with open(f"../../data/by_campaigns_by_days_data/{output_name}.json", "w") as file:
        json.dump(by_campaign_by_day_daily_stats, file)

    print(f"{output_name} created")


