from config.config import *
from functions.data_acquisition_functions.create_countries_for_one_campaign_dataset import create_countries_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]

print(create_countries_for_one_campaign_dataset(vol_id))


