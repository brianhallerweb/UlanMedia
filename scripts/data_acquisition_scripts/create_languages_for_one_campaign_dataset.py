from config.config import *
from functions.data_acquisition_functions.create_languages_for_one_campaign_dataset import create_languages_for_one_campaign_dataset
import sys

vol_id = sys.argv[1]

print(create_languages_for_one_campaign_dataset(vol_id))


