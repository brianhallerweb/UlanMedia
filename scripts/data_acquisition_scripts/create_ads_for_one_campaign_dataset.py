from config.config import *
from functions.data_acquisition_functions.create_ads_for_one_campaign_dataset import create_ads_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]
date_range = sys.argv[2]

print(create_ads_for_one_campaign_dataset(vol_id, date_range))


