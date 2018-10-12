from config.config import *
from datetime import datetime, timedelta
import pytz
import sys
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token 
from functions.data_acquisition_functions.create_by_campaigns_by_widgets_data_set import create_by_campaigns_by_widgets_data_set
from functions.misc.create_pst_date_range import create_pst_date_range 
from functions.misc.get_campaign_sets import get_campaign_sets 

mgid_token = get_mgid_access_token(mgid_login, mgid_password)
vol_token = get_vol_access_token(vol_access_id, vol_access_key)

campaigns = get_campaign_sets()
    
for campaign in campaigns:
    mgid_id = campaign["mgid_id"]
    vol_id = campaign["vol_id"] 

    # yesterday
    dates = create_pst_date_range(2, 1)
    start_date = dates[0]
    end_date = dates[1]
    create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
            str(mgid_id), vol_id, start_date, end_date, f"{vol_id}_yesterday_by_campaigns_by_widgets_data")

    # last 7 days
    dates = create_pst_date_range(8, 1)
    start_date = dates[0]
    end_date = dates[1]
    create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
            str(mgid_id), vol_id, start_date, end_date, f"{vol_id}_seven_by_campaigns_by_widgets_data")

    # last 30 days
    dates = create_pst_date_range(31, 1)
    start_date = dates[0]
    end_date = dates[1]
    create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
            str(mgid_id), vol_id, start_date, end_date, f"{vol_id}_thirty_by_campaigns_by_widgets_data")

    # last 90 days
    dates = create_pst_date_range(90, 1)
    start_date = dates[0]
    end_date = dates[1]
    create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
            str(mgid_id), vol_id, start_date, end_date, f"{vol_id}_ninety_by_campaigns_by_widgets_data")

    # last 180 days
    dates = create_pst_date_range(181, 1)
    start_date = dates[0]
    end_date = dates[1]
    create_by_campaigns_by_widgets_data_set(mgid_token, vol_token,
            str(mgid_id), vol_id, start_date, end_date, f"{vol_id}_oneeighty_by_campaigns_by_widgets_data")