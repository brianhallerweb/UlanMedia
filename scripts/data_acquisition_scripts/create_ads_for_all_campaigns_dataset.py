from config.config import *
from functions.data_acquisition_functions.create_ads_for_all_campaigns_dataset import create_ads_for_all_campaigns_dataset
import sys

# date_range = sys.argv[1]
date_range = "oneeighty"

print(create_ads_for_all_campaigns_dataset(date_range))


