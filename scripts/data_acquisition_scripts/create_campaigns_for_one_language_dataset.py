from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_language_dataset import create_campaigns_for_one_language_dataset
import sys

language_name = sys.argv[1]

print(create_campaigns_for_one_language_dataset(language_name))


