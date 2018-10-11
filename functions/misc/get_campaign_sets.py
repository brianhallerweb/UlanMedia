import requests
from datetime import datetime
import sys
import pandas as pd
from pandas.compat import StringIO
from functions.misc.send_email import send_email

def get_campaign_sets():
    try:
        res = requests.get("https://www.ulanmedia.com/mgid/campaign_sets.txt")
        res.raise_for_status()
        campaign_sets_data = StringIO("vol_id\tmgid_id\tname\tmax_lead_cpa\tmax_sale_cpa\n" +
                str(res.text))
        return pd.read_csv(campaign_sets_data, sep="\t").to_dict("records")
    except requests.exceptions.RequestException as e:
            print("Failed to update campaign sets")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_campaign_sets() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

