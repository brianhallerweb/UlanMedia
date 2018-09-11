from datetime import datetime, timedelta
import pytz
from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_by_campaigns_by_days_data_set import create_by_campaigns_by_days_data_set
from functions.misc.send_email import send_email
import pandas as pd
import json

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(50)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow())
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

create_by_campaigns_by_days_data_set(vol_token, mgidVolTrafficSourceId,
        start_date, end_date, "by_campaigns_by_days_data")



