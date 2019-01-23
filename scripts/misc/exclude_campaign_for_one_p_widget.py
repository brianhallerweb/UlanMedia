from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.misc.exclude_campaign_for_one_p_widget import exclude_campaign_for_one_p_widget
import sys

widget_id = sys.argv[1]
campaign_id = sys.argv[2]

mgid_token = get_mgid_access_token(mgid_login, mgid_password)

print(exclude_campaign_for_one_p_widget(mgid_token, mgid_client_id, widget_id,
    campaign_id))

