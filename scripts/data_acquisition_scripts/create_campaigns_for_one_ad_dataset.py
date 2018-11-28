from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_ad_dataset import create_campaigns_for_one_ad_dataset

# ad_image = sys.argv[0]
# date_range = sys.argv[1]
ad_image = "cashpile3.jpg"
date_range = "seven"

create_campaigns_for_one_ad_dataset(ad_image, date_range)

print(f"{date_range} ads for all campaigns dataset created")

