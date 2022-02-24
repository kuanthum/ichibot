from numpy import exp2
import pandas as pd

from pybit import HTTP
import time
from datetime import datetime
import calendar


from pybit import HTTP, WebSocket

session = HTTP(
    endpoint = 'https://api-testnet.bybit.com',
    api_key = "WJYwnYE2Qv6XUrEMwW",
    api_secret = "AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)



while True:

    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    since = unixtime - 60 * 60 *24*200

    response=session.query_kline(symbol='BTCUSD',interval="D",**{'from':since})['result']

    df = pd.DataFrame(response)

    df = df['close']


    exp1 = df.ewm(span = 12, adjust = False).mean()
    exp2 = df.ewm(span = 26, adjust = False).mean()
    macd = exp1-exp2
    exp3 = macd.ewm(span = 9, adjust = False).mean()

    print('MACD: ', macd.iloc[-1])
    print('Signal: ',exp3.iloc[-1])

    test1=exp3.iloc[-2]-macd.iloc[-2]
    test2=exp3.iloc[-1]-macd.iloc[-1]

    call = 'No trade'

    if test1<0 and test2>0:
        call='Sell'

    if test1>0 and test2<0:
        call='Buy'

    print('Trade Recomendation: ', call)


