from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.create_c_widgets_for_one_p_widget_for_one_campaign_dataset import create_c_widgets_for_one_p_widget_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]
p_widget = sys.argv[2]
date_range = sys.argv[3]
max_rec_bid = sys.argv[4]

print(create_c_widgets_for_one_p_widget_for_one_campaign_dataset(mgid_token, vol_id, p_widget, date_range, max_rec_bid))

