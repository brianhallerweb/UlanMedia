import requests
import sys


try:
    res = requests.get("https://www.ulanmedia.com/mgid/campaign_sets.txt")
    res.raise_for_status()
    with open("../../config/campaign_sets.txt", "w") as file:
        file.write("vol_id\tmgid_id\tname\tmax_lead_cpa\tmax_sale_cpa\n")
        file.write(res.text)

    print("update complete")
except requests.exceptions.RequestException as e:
        print("Failed to update campaign sets")
        print(e)
        sys.exit()
