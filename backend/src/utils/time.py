def get_timestamp_now():
    import datetime
    return (datetime.datetime.now()).replace(tzinfo=datetime.timezone.utc).timestamp()