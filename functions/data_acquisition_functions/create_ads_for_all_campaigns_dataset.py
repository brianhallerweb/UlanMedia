from config.config import *
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.data_acquisition_functions.combine_mgid_vol_ads_data import combine_mgid_vol_ads_data
from functions.misc.create_vol_date_range import create_vol_date_range
import json


def create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range):

    date_range_lookup = {"yesterday": 1, "seven": 7, "thirty": 30, "ninety":
            90, "oneeighty": 180}
    days_ago = date_range_lookup[date_range]

    vol_dates = create_vol_date_range(days_ago, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]

    vol_data = get_vol_ads_data(vol_token, vol_start_date, vol_end_date, mgid_timezone) 
    mgid_data = get_mgid_ads_data(mgid_token, mgid_client_id)
    combined_data = combine_mgid_vol_ads_data(mgid_data, vol_data)

    with open(f"../../data/ads_for_all_campaigns/{date_range}_ads_for_all_campaigns_dataset.json", "w") as file:
        json.dump(combined_data, file)


    









