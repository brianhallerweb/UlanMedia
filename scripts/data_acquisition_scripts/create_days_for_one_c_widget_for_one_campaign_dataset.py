from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.data_acquisition_functions.create_days_for_one_c_widget_for_one_campaign_dataset import create_days_for_one_c_widget_for_one_campaign_dataset
import sys

c_widget_id = sys.argv[1]
campaign_id = sys.argv[2]

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]


print(create_days_for_one_c_widget_for_one_campaign_dataset(vol_token,
    vol_start_date, vol_end_date, c_widget_id, campaign_id))
