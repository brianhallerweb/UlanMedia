from config.config import *
from functions.data_acquisition_functions.create_offers_for_all_flow_rules_dataset import create_offers_for_all_flow_rules_dataset
import sys

date_range = sys.argv[1]

print(create_offers_for_all_flow_rules_dataset(date_range))


