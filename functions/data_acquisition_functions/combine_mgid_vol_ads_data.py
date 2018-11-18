from config.config import *

def combine_mgid_vol_ads_data(mgid_data, vol_data):
    # This function will combine the mgid ads data and the vol ads data. Both
    # data sets are dictionaries with keys = ad id and values = dictionaries of
    # data for that ad id. Each ad in each campaign has a unique ad id.
    # However, ads are actually repeated across multiple campaigns. The
    # identification for each truly unique ad is its image name (image). So,
    # combining the ads data from mgid and vol means creating a new dictionary
    # with key = image and value = dictionary of summary stats for each ad
    # comibined across all campaigns. 
    
    # start by combining mgid and vol by ad_id
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
    combined_ads_data_by_ad_id = mgid_data    

    # Now create a new dictionary with keys = image
    combined_ads_data_by_ad_image = {}   
    for ad in combined_ads_data_by_ad_id.values():
        image = ad["image"]
        if image in combined_ads_data_by_ad_image:
            combined_ads_data_by_ad_image[image]["clicks"] += ad["clicks"] 
            combined_ads_data_by_ad_image[image]["conversions"] += ad["conversions"] 
            combined_ads_data_by_ad_image[image]["cost"] += ad["cost"] 
            combined_ads_data_by_ad_image[image]["revenue"] += ad["revenue"] 
        else:
            combined_ads_data_by_ad_image[image] = ad

    return combined_ads_data_by_ad_image

