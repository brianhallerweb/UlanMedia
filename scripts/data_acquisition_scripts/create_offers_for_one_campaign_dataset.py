from config.config import *
from functions.data_acquisition_functions.create_offers_for_one_campaign_dataset import create_offers_for_one_campaign_dataset
import sys

date_range = sys.argv[1]
vol_id = sys.argv[2]

print(create_offers_for_one_campaign_dataset(date_range, vol_id))


