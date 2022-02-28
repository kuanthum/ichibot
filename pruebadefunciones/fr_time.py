from datetime import datetime
import calendar

#unixtime get for market data
now = datetime.utcnow()
unixtime = calendar.timegm(now.timetuple())
f_time = unixtime - 60 * 60 * 24*100