from functions.data_acquisition_functions.create_c_widgets_for_one_p_widget_dataset import create_c_widgets_for_one_p_widget_dataset
from functions.misc.get_campaign_sets import get_campaign_sets 
import sys

p_widget_id = sys.argv[1]
date_range = sys.argv[2]

campaigns = get_campaign_sets()

create_c_widgets_for_one_p_widget_dataset(campaigns, p_widget_id, date_range)

