from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
import requests

mgid_token = get_mgid_access_token(mgid_login, mgid_password)

def exclude_campaign_for_one_p_widget(token, client_id, campaign_id, widget_id):
    url = f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns/{campaign_id}?token={token}";
    res = requests.patch(url, 
        headers ={"Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"}, 
        data = {"widgetsFilterUid": f"include,except,{widget_id}"})
    
    return res.json()


