from os import lstat
from numpy import exp2
import pandas as pd

from pybit import HTTP
import time
from datetime import datetime
import calendar

from colorama import init

init()

from pybit import HTTP, WebSocket

#----CONECTION----
session = HTTP(
    endpoint = 'https://api-testnet.bybit.com',
    api_key = "WJYwnYE2Qv6XUrEMwW",
    api_secret = "AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)


#----ENTRADAS----
#desde = input('Desde: ')
#desde2 = int(desde)
now = datetime.utcnow()
unixtime = calendar.timegm(now.timetuple())
#since = unixtime - 60 * 60 *24*(desde2)
_26dias = unixtime - 60 * 60 * 24*0.135
#print(since)

#intervalo = input('Intervalo: ')

#symb = input('Simbolo: ')

print(" ")
print("------------------------------------------------------------------------")
print(" ")

#----DATA----
#PREGUNTAR A NICO PORQUE EL RESULT
response = session.query_kline(symbol='BTCUSDT',interval='1',from_time=_26dias)['result']
df = pd.DataFrame(response)

print(df)