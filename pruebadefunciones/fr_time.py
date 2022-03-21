from datetime import datetime
import calendar

#unixtime get for market data
days = 100
def f_time_func(days):
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    f_time = unixtime - 60 * 60 * 24*days
    return f_time

if __name__ == "__main__":
    f_time_func()
# 1min = 60s
# 1min*200 = 12000s
# 1day = 60s*60m*24 = 86400s
# 1day/1min*200 = 7,2
# 86400s/7,2 = 12000s
# 24h/7,2 = 3.33

#for m1 days = 0.135

# s = 'AVAXUSDT'
# interval = 5
# days = 0.65