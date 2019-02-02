from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token
from functions.misc.exclude_p_widget_for_all_campaigns import exclude_p_widget_for_all_campaigns
import sys

# This script will exclude all campaigns for one p widget

widget_id = sys.argv[1]
# widget_id = "5676562"

mgid_token = get_mgid_access_token(mgid_login, mgid_password)

print(exclude_p_widget_for_all_campaigns(mgid_token, mgid_client_id, widget_id))
