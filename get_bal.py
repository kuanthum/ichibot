
from sqlite3 import Timestamp
from pybit import HTTP
from datetime import datetime
from pybit import HTTP, WebSocket
import calendar

now = datetime.utcnow()
unixtime = calendar.timegm(now.timetuple())

session = HTTP(
    endpoint = 'https://api-testnet.bybit.com',
    api_key = "WJYwnYE2Qv6XUrEMwW",
    api_secret = "AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2",
    recv_window = 5000,

)

balance = session.get_wallet_balance(
    coin="USDT",
    timpestamp = unixtime    
)

lst = list(balance.values())
lst2 = list(lst[4].values())
lst3 = list(lst2[0].items())

print(lst3[1])


