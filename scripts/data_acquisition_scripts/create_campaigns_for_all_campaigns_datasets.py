from config.config import *
from functions.data_acquisition_functions.create_campaigns_for_one_ad_dataset import create_campaigns_for_one_ad_dataset

ad_id = sys.argv[1]
date_range = sys.argv[2]

create_campaigns_for_all_campaigns_dataset(vol_token, mgid_token, days_ago,
        f"{date_range}_campaigns_for_one_ad_dataset")





