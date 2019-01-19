import requests
from datetime import datetime
import sys
from functions.misc.send_email import send_email

def get_blacklist():
    try:
        # res = requests.get("https://www.ulanmedia.com/mgid/widgets_blacklist.txt")
        # res.raise_for_status()
        # return res.text.splitlines()
        res = requests.get("https://ulanmedia.brianhaller.net/api/readblacklist")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
            print("Failed to update campaign sets")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_campaign_sets() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

