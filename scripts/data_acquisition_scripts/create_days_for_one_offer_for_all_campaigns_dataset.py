from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.data_acquisition_functions.create_days_for_one_offer_for_all_campaigns_dataset import create_days_for_one_offer_for_all_campaigns_dataset
import sys

offer_name = sys.argv[1]
# offer_name = "1k Daily Profit EN (bin: southAfrica - English)"

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

days = create_days_for_one_offer_for_all_campaigns_dataset(vol_token, vol_start_date,
        vol_end_date, offer_name)

print(days)

