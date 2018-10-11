import requests
from datetime import datetime
import sys
from functions.misc.send_email import send_email

def get_mgid_campaign_costs(token, client_id, start, end):
    try:
        res = requests.get(
        f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns-stat?token={token}&dateInterval=interval&startDate={start}&endDate={end}")
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_campaign_costs")
        send_email("brianshaller@gmail.com", "Failed -                get_mgid_campaign_costs() at " + str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
