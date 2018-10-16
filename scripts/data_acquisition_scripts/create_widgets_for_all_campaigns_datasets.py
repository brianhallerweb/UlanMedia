from functions.data_acquisition_functions.create_widgets_for_all_campaigns_dataset import create_widgets_for_all_campaigns_dataset
from functions.misc.get_campaign_sets import get_campaign_sets 


campaigns = get_campaign_sets()

#############################################
# create a data set for yesterday 
date_range = "yesterday"

create_widgets_for_all_campaigns_dataset(campaigns, date_range)

print(f"{date_range} widgets for all campaigns dataset created")

#############################################
# create a data set for 7 days 
date_range = "seven"

create_widgets_for_all_campaigns_dataset(campaigns, date_range)

print(f"{date_range} widgets for all campaigns dataset created")

#############################################
# create a data set for 30 days 
date_range = "thirty"

create_widgets_for_all_campaigns_dataset(campaigns, date_range)

print(f"{date_range} widgets for all campaigns dataset created")
#############################################
# create a data set for 90 days 
date_range = "ninety"

create_widgets_for_all_campaigns_dataset(campaigns, date_range)

print(f"{date_range} widgets for all campaigns dataset created")
#############################################
# create a data set for 180 days 
date_range = "oneeighty"

create_widgets_for_all_campaigns_dataset(campaigns,  date_range)

print(f"{date_range} widgets for all campaigns dataset created")
