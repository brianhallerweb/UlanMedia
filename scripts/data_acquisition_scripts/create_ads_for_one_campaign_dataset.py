from config.config import *
from functions.data_acquisition_functions.create_ads_for_one_campaign_dataset import create_ads_for_one_campaign_dataset
import sys

# vol_id = sys.argv[1]
# date_range = sys.argv[2]
vol_id = "4ff2a836-8790-4e07-9f45-98b05c3a393a"
date_range = "seven"

create_ads_for_one_campaign_dataset(vol_id, date_range)


