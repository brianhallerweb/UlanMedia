from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_ad_dataset import create_campaigns_for_one_ad_dataset
import sys

ad_image = sys.argv[1]
date_range = sys.argv[2]

create_campaigns_for_one_ad_dataset(ad_image, date_range)


