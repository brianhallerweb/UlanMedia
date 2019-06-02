from config.config import *
import sys
import json
from functions.data_acquisition_functions.create_campaigns_for_one_p_widget_dataset import create_campaigns_for_one_p_widget_dataset

widget_id = sys.argv[1]
date_range = sys.argv[2]
max_rec_bid = sys.argv[3]
default_coeff = sys.argv[4]

print(create_campaigns_for_one_p_widget_dataset(widget_id, date_range, max_rec_bid, default_coeff, f"{widget_id}_{date_range}_campaigns_for_one_p_widget_dataset"))



