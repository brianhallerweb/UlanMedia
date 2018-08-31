from data.seven_campaigns_data import seven_campaigns_data
from functions.data_analysis_functions.create_df import create_df
from functions.data_analysis_functions.prepend_report import prepend_report 

create_df(seven_campaigns_data, "seven_campaigns_data")
prepend_report("seven_campaigns_data")
