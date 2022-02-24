
import calendar
from datetime import datetime

from pybit import HTTP
session = HTTP("https://api-testnet.bybit.com")
server_time = session.server_time()['time_now']

recv_window = 5000

now = datetime.utcnow()
unixtime = calendar.timegm(now.timetuple())

print(unixtime)
print("server_time: ",server_time)

#rule: server_time - recv_window <= timestamp < server_time + 1000