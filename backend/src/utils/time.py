import datetime

def get_timestamp_now():
    import datetime
    return (datetime.datetime.now()).timestamp()

def is_current_week(target_date: datetime.datetime):
    now = datetime.datetime.now()
    monday = now - datetime.timedelta(days=now.weekday())
    sunday = monday + datetime.timedelta(days=6)
    return monday <= target_date <= sunday

def is_today(target_date: datetime.datetime):
    today = datetime.datetime.now().date()
    return target_date == today

def unix_to_datetime(unix_timestamp):
    return datetime.datetime.fromtimestamp(int(unix_timestamp))

def seconds_ago(past_time):
    now = datetime.datetime.now()
    delta = now - past_time
    return int(delta.total_seconds())