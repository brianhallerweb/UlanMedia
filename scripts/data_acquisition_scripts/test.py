from config.config import *
from functions.data_acquisition_functions.get_mgid_access_token import get_mgid_access_token 

mgid_token = get_mgid_access_token(mgid_login, mgid_password)
print(mgid_token)
