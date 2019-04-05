from config.config import *
from functions.data_acquisition_functions.create_countries_dataset import create_countries_dataset
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range

token = get_vol_access_token(vol_access_id, vol_access_key)

dates = create_vol_date_range(180, mgid_timezone)
start_date = dates[0]
end_date = dates[1]

create_countries_dataset(token, start_date, end_date)

print("one eighty countries dataset created")
