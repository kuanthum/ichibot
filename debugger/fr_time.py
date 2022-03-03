from datetime import datetime
import calendar

#unixtime get for market data
candle_data = 100

def f_time_func():
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    f_time = unixtime - 60 * 60 * 24*candle_data
    return f_time