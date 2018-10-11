from config.config import *
from datetime import datetime, timedelta
import pytz
import sys
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token 
from functions.data_acquisition_functions.create_by_campaigns_by_widgets_data_set import create_by_campaigns_by_widgets_data_set
from functions.misc.create_pst_date_range import create_pst_date_range 

mgid_token = get_mgid_access_token(mgid_login, mgid_password)
vol_token = get_vol_access_token(vol_access_id, vol_access_key)

# this script a creates by_campaign_by_widget json data sets for a particular
# date range
# The data sets include accumulated data on every widget for one campaign
# campaign info (mgid_id, vol_id, and dateRange) are passed from react

mgid_id = sys.argv[1] 
vol_id = sys.argv[2] 
date_range = sys.argv[3] 

end_date_translator ={"yesterday": 2, "seven": 8, "thirty": 31, "ninety": 91,
        "oneeighty": 181}

# dates is [start date, end date]
dates = create_pst_date_range(end_date_translator[date_range], 1)
start_date = dates[0]
end_date = dates[1]

create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
mgid_id,
vol_id, start_date, end_date, f"{vol_id}_{date_range}_by_campaigns_by_widgets_data")

