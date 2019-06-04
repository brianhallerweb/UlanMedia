from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.create_c_widgets_for_one_campaign_dataset import create_c_widgets_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]
date_range = sys.argv[2]
max_rec_bid = sys.argv[3]

print(create_c_widgets_for_one_campaign_dataset(mgid_token, vol_id, date_range, max_rec_bid))

