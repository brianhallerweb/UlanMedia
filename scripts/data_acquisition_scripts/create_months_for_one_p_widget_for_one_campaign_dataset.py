from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range
from functions.data_acquisition_functions.create_months_for_one_p_widget_for_one_campaign_dataset import create_months_for_one_p_widget_for_one_campaign_dataset
import sys

p_widget_id = sys.argv[1]
campaign_id = sys.argv[2]
# p_widget_id = "5679842"
# campaign_id = "39eded96-4619-4c00-b0e6-bfdc622c894c"

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

vol_dates = create_vol_date_range(180, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]


print(create_months_for_one_p_widget_for_one_campaign_dataset(vol_token,
    vol_start_date, vol_end_date, p_widget_id, campaign_id))

