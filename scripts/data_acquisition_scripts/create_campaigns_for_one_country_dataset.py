from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_country_dataset import create_campaigns_for_one_country_dataset
import sys

country_name = sys.argv[1]

print(create_campaigns_for_one_country_dataset(country_name))


