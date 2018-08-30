import requests
import datetime
import sys
from functions.misc.send_email import send_email


def get_mgid_access_token(login, password):
    try:
        res = requests.post("https://api.mgid.com/v1/auth/token",  headers={"Content-type":
                                                                            "application/x-www-form-urlencoded", "Cache-Control":
                                                                            "no-cache"}, data={"email": login, "password":
                                                                                               password})
        try:
            return res.json()["token"]
        except:
            send_email("brianshaller@gmail.com", "Failed - mgid token access at " +
                       str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), "Http status code error - mgid token access failed.")
            sys.exit()
    except requests.exceptions.RequestException as e:
        print("Failed - get_mgid_access_token()")
        send_email("brianshaller@gmail.com", "Failed - get_mgid_access_token() at " +
                   str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), e)
        sys.exit()


