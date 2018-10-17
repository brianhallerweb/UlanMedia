from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_days_for_one_campaign_dataset import create_days_for_one_campaign_dataset

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

days_ago = 50

create_days_for_one_campaign_dataset(vol_token, mgidVolTrafficSourceId,
        days_ago, "days_for_one_campaign_dataset")



