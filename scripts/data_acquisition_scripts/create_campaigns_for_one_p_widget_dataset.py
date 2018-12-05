from config.config import *
from datetime import datetime, timedelta
import sys
import json
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token 
from functions.data_acquisition_functions.create_campaigns_for_one_p_widget_dataset import create_campaigns_for_one_p_widget_dataset
from functions.misc.get_campaign_sets import get_campaign_sets

widget_id = sys.argv[1]
date_range = sys.argv[2]

create_campaigns_for_one_p_widget_dataset(widget_id, date_range,
        f"{widget_id}_{date_range}_campaigns_for_one_p_widget_dataset")



