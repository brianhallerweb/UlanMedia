from config.config import *
import sys
import json
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.data_acquisition_functions.get_mgid_ads_data import get_mgid_ads_data
from functions.data_acquisition_functions.get_vol_ads_data import get_vol_ads_data
from functions.misc.create_vol_date_range import create_vol_date_range

def combine_mgid_vol_ads_data(mgid_token, vol_token,date_range, mgid_data, vol_data):
    # This function will combine the mgid ads data and the vol ads data. Both
    # data sets are dictionaries with keys = ad id and values = dictionaries of
    # data for that ad id. 
    
    # combining mgid and vol by ad_id
    # For convenience, Vol data is added to the existing mgid data. The name of
    # the combined data is changed from mgid_data to combined_ads_data_by_ad_id
    # afterward.
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
    combined_ads = mgid_data    

    with open(f"../../data/ads/{date_range}_ads_dataset.json", "w") as file:
        json.dump(combined_ads, file)


