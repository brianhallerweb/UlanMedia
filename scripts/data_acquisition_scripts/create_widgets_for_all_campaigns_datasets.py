from functions.data_acquisition_functions.create_all_widgets_list import create_all_widgets_list
from functions.data_acquisition_functions.create_widgets_for_all_campaigns_dataset import create_widgets_for_all_campaigns_dataset
from functions.misc.get_campaign_sets import get_campaign_sets 


campaigns = get_campaign_sets()

#############################################
# create a data set for yesterday 
date_range = "yesterday"

all_widgets = create_all_widgets_list(campaigns, date_range)

create_widgets_for_all_campaigns_dataset(campaigns, all_widgets, date_range)

#############################################
# create a data set for 7 days 
date_range = "seven"

all_widgets = create_all_widgets_list(campaigns, date_range)

create_widgets_for_all_campaigns_dataset(campaigns, all_widgets, date_range)

#############################################
# create a data set for 30 days 
date_range = "thirty"

all_widgets = create_all_widgets_list(campaigns, date_range)

create_widgets_for_all_campaigns_dataset(campaigns, all_widgets, date_range)

#############################################
# create a data set for 90 days 
date_range = "ninety"

all_widgets = create_all_widgets_list(campaigns, date_range)

create_widgets_for_all_campaigns_dataset(campaigns, all_widgets, date_range)

#############################################
# create a data set for 180 days 
date_range = "oneeighty"

all_widgets = create_all_widgets_list(campaigns, date_range)

create_widgets_for_all_campaigns_dataset(campaigns, all_widgets, date_range)


