from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_offer_dataset import create_campaigns_for_one_offer_dataset
import sys

date_range = sys.argv[1]
offer_id = sys.argv[2]

print(create_campaigns_for_one_offer_dataset(date_range, offer_id))


