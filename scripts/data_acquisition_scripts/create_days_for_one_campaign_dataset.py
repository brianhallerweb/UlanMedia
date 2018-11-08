from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_days_for_one_campaign_dataset import create_days_for_one_campaign_dataset

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

days_ago = 50

# one argument is for mgid token but I am not using it yet
# so i filled it with "nomgidtoken"
create_days_for_one_campaign_dataset(vol_token, "nomgidtoken",
        days_ago, "days_for_one_campaign_dataset")



