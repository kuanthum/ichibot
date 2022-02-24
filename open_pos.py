
from pybit import HTTP
from datetime import datetime
import calendar
import pandas as pd

now = datetime.utcnow()
unixtime = calendar.timegm(now.timetuple())
_26dias = unixtime - 60 * 60 * 24*100

session = HTTP("https://api-testnet.bybit.com"
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)


print(session.query_kline(
    symbol="BTCUSDT",
    interval=1,
    limit=2,
    from_time=_26dias
)['result']


df = pd.DataFrame(response)

stop_loss_t = lastprice*0.05

session = HTTP("https://api-testnet.bybit.com", api_key="WJYwnYE2Qv6XUrEMwW", api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2")
print(session.place_active_order(
    symbol="BTCUSDT",
    side="Buy",
    order_type="Market",
    qty=0.002,
    time_in_force="GoodTillCancel",
    reduce_only = False,
    close_on_trigger = False
))

