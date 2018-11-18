from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.create_ads_for_all_campaigns_dataset import create_ads_for_all_campaigns_dataset

vol_token = get_vol_access_token(vol_access_id, vol_access_key)
mgid_token = get_mgid_access_token(mgid_login, mgid_password)

#############################################
# create a data set for yesterday 
date_range = "yesterday"

create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range)

print(f"{date_range} ads for all campaigns dataset created")

#############################################
# create a data set for the last seven days
date_range = "seven"

create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range)

print(f"{date_range} ads for all campaigns dataset created")

#############################################
# create a data set for the last thirty days
date_range = "thirty"

create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range)

print(f"{date_range} ads for all campaigns dataset created")

#############################################
# create a data set for the last ninety days
date_range = "ninety"

create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range)

print(f"{date_range} ads for all campaigns dataset created")

#############################################
# create a data set for the last oneeighty days
date_range = "oneeighty"

create_ads_for_all_campaigns_dataset(mgid_token, vol_token, date_range)

print(f"{date_range} ads for all campaigns dataset created")

