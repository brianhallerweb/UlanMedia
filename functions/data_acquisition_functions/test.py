mgid_id = '511288'
widget_id = '56995760'


# the above combination is incorrectly being classified as inactive
# http://localhost:8080/pwidgetsforonecampaign/0950c470-e4e3-4963-bebe-48c65d13a63e/bin_europe-t1_english_mobile_cpc_0.02/
# when searched for 7 days, it comes back as inactive when it is active

# why? 

# run the included function to see it is in included

from functions.data_acquisition_functions.get_mgid_included_widgets_by_campaign import get_mgid_included_widgets_by_campaign
from functions.misc.get_campaign_sets import get_campaign_sets
from functions.misc.create_mgid_date_range import create_mgid_date_range
from config.config import *
import pprint
from config.mgid_token import mgid_token
pp=pprint.PrettyPrinter(indent=2)

mgid_dates = create_mgid_date_range(90, mgid_timezone)
start_date = mgid_dates[0]
end_date = mgid_dates[1]

# included_widgets = get_mgid_included_widgets_by_campaign(mgid_token, mgid_id, start_date,
        # end_date)

# if widget_id in included_widgets:
    # print("yes")
# else:
    # print("no")
###################################
# So the widget is not included 
# the widget is definitley a part of the campaign so I need to figure out why it
# isn't included

# response = get_mgid_included_widgets_by_campaign(mgid_token, mgid_id, start_date,
        # end_date)

# for key in response[mgid_id]['2019-01-30_2019-04-29']:
    # if key == widget_id:
        # pp.pprint(key)
        # pp.pprint(widget_id)

# now it appears that it is in there?

# try to the old way again

###################################

included_widgets = get_mgid_included_widgets_by_campaign(mgid_token, mgid_id, start_date,
        end_date)

if widget_id in included_widgets:
    print("yes")
else:
    print("no")
