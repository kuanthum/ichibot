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
_26dias = unixtime - 60 * 60 * 24*100
#print(since)

#intervalo = input('Intervalo: ')

#symb = input('Simbolo: ')

print(" ")
print("------------------------------------------------------------------------")
print(" ")

#----DATA----
#PREGUNTAR A NICO PORQUE EL RESULT
response = session.query_kline(symbol='BTCUSDT',interval='D',from_time=_26dias)['result']
df = pd.DataFrame(response)

candle_c = df['close']
candle_h = df['high']
candle_l = df['low']
lastprice = candle_c.iloc[-1]
print("Lastprice: ",(lastprice))


#----ICHIMOKU DATA----

#TENKAN-SEN (convertion line)
thigh = candle_h[-9:].max()
tlow = candle_l[-9:].min()
tenkan_sen = (thigh+tlow)/2
print("Tenkan sen: ", tenkan_sen, " tested ok")

#TENKAN LOOKBACK
thigh26 = candle_h[-9-26:-26].max()
tlow26 = candle_l[-9-26:-26].min()
tenkan_sen_26 = (thigh26+tlow26)/2
print("Tenkan sen look back: ", tenkan_sen_26, " tested ok")

#KIJUN-SEN (base line) 
khigh = candle_h[-26:].max()
klow = candle_l[-26:].min()
kijun_sen = (khigh+klow)/2
print("Kijun sen: ",kijun_sen ," tested ok") 

#KIJUN LOOKBACK
khigh = candle_h[-26-26:-26].max()
klow = candle_l[-26-26:-26].min()
kijun_sen_26 = (khigh+klow)/2
print("Kijun sen lookback: ",kijun_sen_26, " tested ok")

#----KUMO CLOUD----

#KUMO AHEAD

#SENKOU SPAN A 
senkou_span_a = (tenkan_sen+kijun_sen)/2
print("Senkou span a: ",(senkou_span_a), "tested ok")

#SENKOU SPAN B 
ssbh = candle_h[-52:].max()
ssbl = candle_l[-52:].min()
senkou_span_b = (ssbh+ssbl)/2
print("Senkou span b: ",(senkou_span_b), "tested ok")

#KUMONOW

#NOWsenkouA
senkou_span_a_now = (tenkan_sen_26+kijun_sen_26)/2
print("Senkou span a lookback: ",(senkou_span_a_now)," tested ok")

#NOWsenkowB
ssbh1 = candle_h[-52-26:-25].max()
ssbl1 = candle_l[-52-26:-26].min()
senkou_span_b_now = (ssbh1+ssbl1)/2
print("Senkou span b lookback: ",(senkou_span_b_now), "tested ok")


print(" ")
print("------------------------------------------------------------------------")
print(" ")

#----ICHI TEST----

#TK CROSS

def tk_cross():
    if tenkan_sen > kijun_sen:
        return 1 
    else:
        return -1    

print("TK cross is: ",tk_cross())

#KUMO AHEAD
def kumo_cloud():
    if senkou_span_a > senkou_span_b:
        return 1
    else:
        return -1

print("Kumo ahead is: ",kumo_cloud())

#KUMO VS PRICE
def kumo_cloud_now():
    if senkou_span_a_now > senkou_span_b_now:
        if lastprice > senkou_span_a_now:
            return 1 
        elif lastprice < senkou_span_b_now:
            return -1
        else:
            return 0
    elif lastprice < senkou_span_a_now:
            return -1
    elif lastprice > senkou_span_b_now:
            return 1
    else:
        return 0

print("Price vs Kumo is: ",kumo_cloud_now())

#CHIKOU
chikou = candle_c.iloc[-26]
def chikou_test():
    if lastprice > chikou:
        return 1
    else:
        return -1


print("Chikou is: ",chikou_test())

print(" ")
print("------------------------------------------------------------------------")
print(" ")


puntaje = (tk_cross() + kumo_cloud() + kumo_cloud_now() + chikou_test())

print("BTCUSDT", puntaje)

def commend():
    if puntaje == 4:
        return "Go LONG"
    elif puntaje == -4:
        return "Go SHORT"
    else:
        return "Go SLEEP"

print(commend())

print(" ")
print("------------------------------------------------------------------------")
print(" ")

