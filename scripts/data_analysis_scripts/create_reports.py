from data.yesterday_campaigns_data import yesterday_campaigns_data
from data.seven_campaigns_data import seven_campaigns_data 
from data.thirty_campaigns_data import thirty_campaigns_data 
from data.ninety_campaigns_data import ninety_campaigns_data 
from data.oneeighty_campaigns_data import oneeighty_campaigns_data 
from functions.data_analysis_functions.create_df import create_df
from functions.data_analysis_functions.prepend_report import prepend_report 

all_data = { "yesterday_campaigns_data": yesterday_campaigns_data,
        "seven_campaigns_data": seven_campaigns_data,
        "thirty_campaigns_data": thirty_campaigns_data,
        "ninety_campaigns_data": ninety_campaigns_data,
        "oneeighty_campaigns_data": oneeighty_campaigns_data
        }

for data in all_data:
    create_df(all_data[data], data)
    prepend_report(data)

print("all reports created")
