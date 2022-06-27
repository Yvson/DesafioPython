""" Test Functions """
from src.api.utils.format_date import format_datetime



def test_format_date():
    """
    Tests the conversion process from UNIX Timestamp (in milliseconds) to a specific date format - "%d/%m/%Y - %H:%M:%S"
    """
    unix_timestamp_milliseconds = 1656163923744 # "25/06/2022 - 09:44:35"
    format_date_result = format_datetime(unix_timestamp_milliseconds) # "%d/%m/%Y - %H:%M:%S"

    assert format_date_result == "25/06/2022 - 10:32:03"


