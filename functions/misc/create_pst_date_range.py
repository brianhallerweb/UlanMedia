from datetime import datetime, timedelta
import pytz

def create_pst_date_range(days_ago_start, days_ago_end):
    start_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago_start)
    start_date_pst = start_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
    end_date_utc = pytz.utc.localize(datetime.utcnow()) - timedelta(days_ago_end)
    end_date_pst = end_date_utc.astimezone(pytz.timezone("America/Los_Angeles"))
    return [start_date_pst.strftime("%Y-%m-%d"),
            end_date_pst.strftime("%Y-%m-%d")]

