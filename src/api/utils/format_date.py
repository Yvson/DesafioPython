from datetime import datetime

def format_datetime(unix_timestamp_milliseconds):
    return datetime.fromtimestamp(unix_timestamp_milliseconds/1000).strftime("%d/%m/%Y - %H:%M:%S")
