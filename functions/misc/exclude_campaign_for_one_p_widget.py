import requests
import json

def exclude_campaign_for_one_p_widget(token, client_id, widget_id, campaign_id):
    url = f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns/{campaign_id}?token={token}";
    res = requests.patch(url, 
        headers ={"Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"}, 
        data = {"widgetsFilterUid": f"include,except,{widget_id}"})
    res.raise_for_status() 
    res = res.json()
    # if successful, this function returns json that looks like this
    # {id: campaign_id}
    return json.dumps(res)



