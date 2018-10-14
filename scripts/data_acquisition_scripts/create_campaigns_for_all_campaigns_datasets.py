from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_all_campaign_conversions_by_traffic_source import get_all_campaign_conversions_by_traffic_source
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.data_acquisition_functions.create_campaigns_for_all_campaigns_dataset import create_campaigns_for_all_campaigns_dataset
from functions.misc.create_pst_date_range import create_pst_date_range
from functions.misc.send_email import send_email

vol_token = get_vol_access_token(vol_access_id, vol_access_key)
mgid_token = get_mgid_access_token(mgid_login, mgid_password)

#############################################
# create a data set for yesterday 
date_range = create_pst_date_range(2, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, start_date, end_date,
        "yesterday_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 7 days 
date_range = create_pst_date_range(8, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, start_date, end_date,
        "seven_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 30 days 

date_range = create_pst_date_range(31, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, start_date, end_date,
        "thirty_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 90 days 
date_range = create_pst_date_range(91, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, start_date, end_date,
        "ninety_campaigns_for_all_campaigns_dataset")

#############################################
# create a data set for 180 days 

date_range = create_pst_date_range(181, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, start_date, end_date,
        "oneeighty_campaigns_for_all_campaigns_dataset")
