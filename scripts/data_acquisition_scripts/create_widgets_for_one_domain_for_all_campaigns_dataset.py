from config.config import *
from functions.data_acquisition_functions.create_widgets_for_one_domain_for_all_campaigns_dataset import create_widgets_for_one_domain_for_all_campaigns_dataset
import sys

date_range = sys.argv[1]
domain = sys.argv[2]
# date_range = "oneeighty" 
# domain = "ru-clip.net"

print(create_widgets_for_one_domain_for_all_campaigns_dataset(date_range, domain))

