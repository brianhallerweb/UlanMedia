from config.config import *
from functions.data_acquisition_functions.create_languages_for_all_campaigns_dataset import create_languages_for_all_campaigns_dataset
import sys

date_range = sys.argv[1]

print(create_languages_for_all_campaigns_dataset(date_range))


