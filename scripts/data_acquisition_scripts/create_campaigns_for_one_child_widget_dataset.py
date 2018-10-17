from config.config import *
from datetime import datetime, timedelta
import pytz
import sys
import json
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token 
from functions.data_acquisition_functions.create_campaigns_for_one_child_widget_dataset import create_campaigns_for_one_child_widget_dataset
from functions.misc.get_campaign_sets import get_campaign_sets


##############################
#example campaign and widget for troubleshooting 
#vol_id = "7f5bb9db-7369-4370-83c9-135d90cb4c44"
#mgid_id = "506244"
#widget_id = "5718588"
#date_range = "seven"
##############################

widget_id = sys.argv[1]
date_range = sys.argv[2]

create_campaigns_for_one_child_widget_dataset(widget_id, date_range,
        f"{widget_id}_{date_range}_campaigns_for_one_child_widget_dataset")



