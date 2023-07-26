import datetime as dt

def parse_time(time_str: str) -> dt.datetime :
    res = dt.datetime.strptime(time_str,  "%d/%m/%Y")
    return res 

def format_date(date: dt.date) -> str :
    return date.strftime("%A %d %B %Y")
