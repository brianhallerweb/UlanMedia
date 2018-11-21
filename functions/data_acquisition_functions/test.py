from config.config import *
import sys
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.misc.create_vol_date_range import create_vol_date_range

# my work on campaigns for one ad in progress

def combine(mgid_data, vol_data, image):
    for ad in mgid_data.values():
        ad_id = ad["ad_id"]  
        if ad_id in vol_data:
            vol_ad_data = vol_data[ad_id]
            ad["clicks"] = vol_ad_data["clicks"]
            ad["cost"] = vol_ad_data["cost"]
            ad["conversions"] = vol_ad_data["conversions"]
            ad["revenue"] = vol_ad_data["revenue"]
        else:
            ad["clicks"] = 0
            ad["cost"] = 0
            ad["conversions"] = 0
            ad["revenue"] = 0 
    combined_ads_data_by_ad_id = mgid_data    

    campaigns_for_one_ad_data = []
    for ad in combined_ads_data_by_ad_id.values():
        if ad["image"] == image:
            campaigns_for_one_ad_data.append(ad)

    return campaigns_for_one_ad_data

vol_token = get_vol_access_token(vol_access_id, vol_access_key)
mgid_token = get_mgid_access_token(mgid_login, mgid_password)


vol_dates = create_vol_date_range(1, mgid_timezone)
vol_start_date = vol_dates[0]
vol_end_date = vol_dates[1]

vol_data = get_vol_ads_data(vol_token, vol_start_date, vol_end_date, mgid_timezone) 
mgid_data = get_mgid_ads_data(mgid_token, mgid_client_id)
data = combine(mgid_data, vol_data, "guy4.jpg")

# add vol_id, mgid_id, and campaign name to each ad
for ad in data:
    print(ad["campaign_id"])

# if you continue like this, you are going to be making a ton of redundant
# requests. 
# you should change the design of all ads scripts so that you save a combined
# data set of each ad in a json file. 
# then you should simply use that data to create all the data sets you need for
# display on the web app. 

