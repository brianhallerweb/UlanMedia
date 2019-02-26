from functions.misc.send_email import send_email
from datetime import datetime

subject = "updated all data on ulanmedia.brianhaller.net at " + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
body = "Read the messages on scripts.brianhaller.net to ensure that all data was updated without any errors."

send_email("brianshaller@gmail.com", subject, body)
send_email("mikeseo@gmail.com", subject, body)

