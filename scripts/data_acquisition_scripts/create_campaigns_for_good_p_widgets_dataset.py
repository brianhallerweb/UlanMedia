from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_good_p_widgets_dataset import create_campaigns_for_good_p_widgets_dataset
import sys

date_range = sys.argv[1]
# date_range = "oneeighty"

print(create_campaigns_for_good_p_widgets_dataset(date_range))



