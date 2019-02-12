from config.config import *
from datetime import datetime, timedelta
import sys
import json
from functions.data_acquisition_functions.create_campaigns_for_one_c_widget_dataset import create_campaigns_for_one_c_widget_dataset

widget_id = sys.argv[1]
date_range = sys.argv[2]

print(create_campaigns_for_one_c_widget_dataset(widget_id, date_range,
        f"{widget_id}_{date_range}_campaigns_for_one_c_widget_dataset"))


