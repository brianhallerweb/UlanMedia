from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.create_p_widgets_for_one_campaign_dataset import create_p_widgets_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]
date_range = sys.argv[2]
max_rec_bid = sys.argv[3]
default_coeff = sys.argv[4]

print(create_p_widgets_for_one_campaign_dataset(mgid_token, vol_id, date_range, max_rec_bid, default_coeff))

