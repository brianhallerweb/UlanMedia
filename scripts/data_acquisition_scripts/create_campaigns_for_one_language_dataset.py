from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_language_dataset import create_campaigns_for_one_language_dataset
import sys

date_range = sys.argv[1]
language_name = sys.argv[2]

print(create_campaigns_for_one_language_dataset(date_range, language_name))


