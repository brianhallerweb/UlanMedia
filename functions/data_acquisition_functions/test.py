from config.config import *
from config.mgid_token import mgid_token
from functions.data_acquisition_functions.get_mgid_excluded_widgets_by_campaign import get_mgid_excluded_widgets_by_campaign

excluded_widgets = get_mgid_excluded_widgets_by_campaign(mgid_token,
        mgid_client_id, '527379')
print(excluded_widgets)

