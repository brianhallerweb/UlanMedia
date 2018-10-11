import requests
from datetime import datetime
import sys
from functions.misc.send_email import send_email

def get_whitelist():
    try:
        res = requests.get("https://www.ulanmedia.com/mgid/widgets_whitelist.txt")
        res.raise_for_status()
        return res.text.splitlines()
    except requests.exceptions.RequestException as e:
            print("Failed to update campaign sets")
            print(e)
            send_email("brianshaller@gmail.com", "Failed - update_campaign_sets() at " +
                   str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
            sys.exit()

