from functions.misc.send_email import send_email
from datetime import datetime

message = "CRON updated all data on ulanmedia.brianhaller.net at " + str(datetime.now().strftime("%Y-%m-%d %H:%M"))

send_email("brianshaller@gmail.com", message, message)
send_email("mikeseo@gmail.com", message, message)

