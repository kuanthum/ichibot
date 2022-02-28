from datetime import datetime
import calendar

#unixtime get for market data
def f_time_func():
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    f_time = unixtime - 60 * 60 * 24*100
    return f_time