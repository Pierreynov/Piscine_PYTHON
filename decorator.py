import datetime as dt
def with_current_date(function):
    def modified_function(*args, **kwargs):
        return function(current_date = dt.date.today(), *args, **kwargs)
    return modified_function