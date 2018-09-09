from datetime import datetime, timedelta
import pytz
from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_all_campaigns_daily_stats import get_all_campaigns_daily_stats
from functions.misc.send_email import send_email

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(8)
start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(1)
end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
start_date = start_date_pst.strftime("%Y-%m-%d")
end_date = end_date_pst.strftime("%Y-%m-%d")
print(start_date + " to " + end_date)

campaigns = get_all_campaigns_daily_stats(vol_token, mgidVolTrafficSourceId,
    start_date, end_date)

print(campaigns)

