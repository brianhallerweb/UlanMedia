from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.combine_mgid_vol_ads_data import combine_mgid_vol_ads_data
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.misc.create_vol_date_range import create_vol_date_range
import sys

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

date_range = "oneeighty"
vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

vol_data = get_vol_ads_data(vol_token, vol_start_date, vol_end_date, mgid_timezone) 

mgid_data = get_mgid_ads_data(mgid_token, mgid_client_id)

combine_mgid_vol_ads_data(mgid_token, vol_token, date_range, vol_start_date,
        vol_end_date, mgid_data, vol_data)

print(f"{date_range} ads dataset created")