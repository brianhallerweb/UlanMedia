from data.thirty_campaigns_data import thirty_campaigns_data
from functions.data_analysis_functions.create_df import create_df
from functions.data_analysis_functions.prepend_report import prepend_report 

create_df(thirty_campaigns_data, "thirty_campaigns_data")
prepend_report("thirty_campaigns_data")
