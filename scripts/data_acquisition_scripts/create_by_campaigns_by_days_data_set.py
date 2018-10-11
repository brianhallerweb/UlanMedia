from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.data_acquisition_functions.create_by_campaigns_by_days_data_set import create_by_campaigns_by_days_data_set
from functions.misc.create_pst_date_range import create_pst_date_range

vol_token = get_vol_access_token(vol_access_id, vol_access_key)

date_range = create_pst_date_range(50, 1)
start_date = date_range[0]
end_date = date_range[1]
print(start_date + " to " + end_date)

create_by_campaigns_by_days_data_set(vol_token, mgidVolTrafficSourceId,
        start_date, end_date, "by_campaigns_by_days_data")



