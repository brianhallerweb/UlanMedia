from datetime import datetime, timedelta
import pytz
from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_all_campaign_conversions_by_traffic_source import get_all_campaign_conversions_by_traffic_source
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_campaign_costs import get_mgid_campaign_costs
from functions.misc.send_email import send_email
import pandas
import json
import sys
from functions.data_acquisition_functions.create_data_set import create_data_set

vol_token = get_vol_access_token(vol_access_id, vol_access_key)
mgid_token = get_mgid_access_token(mgid_login, mgid_password)

#############################################
# create a data set for yesterday 
start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(2)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_data_set(vol_token, mgid_token, start_date, end_date,
        "yesterday_campaigns_data")

#############################################
# create a data set for 7 days 
start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(8)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_data_set(vol_token, mgid_token, start_date, end_date,
        "seven_campaigns_data")

#############################################
# create a data set for 30 days 
start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(31)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_data_set(vol_token, mgid_token, start_date, end_date,
        "thirty_campaigns_data")

#############################################
# create a data set for 90 days 
start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(91)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_data_set(vol_token, mgid_token, start_date, end_date,
        "ninety_campaigns_data")

#############################################
# create a data set for 180 days 
start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(181)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_data_set(vol_token, mgid_token, start_date, end_date,
        "oneeighty_campaigns_data")
