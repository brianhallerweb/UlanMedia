from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_country_dataset import create_campaigns_for_one_country_dataset
import sys

date_range = sys.argv[1]
country_name = sys.argv[2]

print(create_campaigns_for_one_country_dataset(date_range, country_name))


