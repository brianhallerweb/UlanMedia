import requests
import sys
from datetime import datetime
from functions.misc.send_email import send_email
from config.config import *

def get_mgid_daily_stats_data(token, start_date, end_date):
    mgid_url = f"https://api.mgid.com/v1/goodhits/clients/{mgid_client_id}/campaigns-stat?token={token}&dateInterval=interval&startDate={start_date}&endDate={end_date}"
    
    try: 
        res = requests.get(mgid_url)
        res.raise_for_status()
        return res.json()["campaigns-stat"]

    except requests.exceptions.RequestException as e:
        send_email("brianshaller@gmail.com", "Failed - get_mgid_daily_stats_data at " +
        str(datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()
