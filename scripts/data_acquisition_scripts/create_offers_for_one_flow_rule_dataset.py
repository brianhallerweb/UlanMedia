from config.config import *
from functions.data_acquisition_functions.create_offers_for_one_flow_rule_dataset import create_offers_for_one_flow_rule_dataset
import sys

date_range = sys.argv[1]
flow_rule = sys.argv[2]

print(create_offers_for_one_flow_rule_dataset(date_range, flow_rule))


