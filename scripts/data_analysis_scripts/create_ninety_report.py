from data.ninety_campaigns_data import ninety_campaigns_data
from functions.data_analysis_functions.create_df import create_df
from functions.data_analysis_functions.prepend_report import prepend_report 

create_df(ninety_campaigns_data, "ninety_campaigns_data")
prepend_report("ninety_campaigns_data")
