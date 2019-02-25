from functions.misc.send_email import send_email
from datetime import datetime

message = "brianshaller@gmail.com", "updated all data " + str(datetime.now().strftime("%Y-%m-%d %H:%M"))

send_email("brianshaller@gmail.com", message, message)

