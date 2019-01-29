import requests
import json
from functions.misc.get_campaign_sets import get_campaign_sets 

# this probably wont be used
def exclude_p_widget_for_all_campaigns(token, client_id, widget_id):
    campaigns = get_campaign_sets()
    for campaign in campaigns:
        campaign_id = campaign["mgid_id"]
        url = f"https://api.mgid.com/v1/goodhits/clients/{client_id}/campaigns/{campaign_id}?token={token}";
        res = requests.patch(url, 
            headers ={"Content-Type": "application/x-www-form-urlencoded",
                "Cache-Control": "no-cache"}, 
            # data = {"widgetsFilterUid": f"include,except,{widget_id}"})
            # Use the line below ("exlude,except,{widget_id}") when you want to
            # include every campaign. This is useful if you are testing
            # excluding every campaign in a p widget and then want to reverse
            # the action
              data = {"widgetsFilterUid": f"exclude,except,{widget_id}"})
        print(campaign_id)
        print(res.json())
        print(res)
        print("############")
    return json.dumps("exclude_p_widget_for_all_campaigns completed")



