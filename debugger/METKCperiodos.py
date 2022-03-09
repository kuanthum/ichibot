
#More efective tk cross
#example on AVAXUSDT

from api_pybit import sym_data
from fr_time import f_time_func
import config as cfg
from ichi_data import ichi_var
from ichi_test import ichi_test_func

sym_value_list = ['EOSUSDT','D', f_time_func()]
sym_keys_list = ['symbol','interval','from_time']
qki = cfg.symbol_data_func(sym_value_list, sym_keys_list)


z = sym_data(qki)
print(z)
#print(z['close'][-3:None])
x = ichi_var(z)
#print(type(x))
#print(x)
tk_n = ichi_test_func(**x)[3]
#print(tk_cross)

ichi_values = []
symbol = z['symbol']
#ichi_values.append(symbol[1])
candle_c = z['close']
candle_h = z['high']
candle_l = z['low']
lastprice = float(candle_c.iloc[-1])
#ichi_values.append(lastprice)
#print(symbol[1])
#print("Lastprice: ",(lastprice))

c = -9
c2 = -26
last_c = len(z)-1
index = 0
tk_cross = tk_n



while tk_cross == tk_n:
    print('---------- Iteracion: ',index)
    print(c, c2)
    print(last_c)
    print('precio de cierre: ', z['close'].iloc[last_c])
    print('----')

    #TENKAN-SEN (convertion line)
    thigh = float(candle_h[c:last_c].max())
    print('*thigh is: ',thigh)
    tlow = float(candle_l[c:last_c].min())
    print('*tlow is: ', tlow)
    tenkan_sen = (thigh+tlow)/2
    print("Tenkan sen: ", tenkan_sen)

    #KIJUN-SEN (base line) 
    khigh = float(candle_h[c2:last_c].max())
    print('*khigh is: ', khigh)
    klow = float(candle_l[c2:last_c].min())
    print('*klow is: ', klow)
    kijun_sen = (khigh+klow)/2
    print("Kijun sen: ",kijun_sen)

    c = (c-1)
    c2 = (c2-1)
    last_c -= 1

    if tenkan_sen >= kijun_sen:
        tk_cross = 1
    else:
        tk_cross = -1    

    index += 1
    print('------------------------------------')
print(index)


# #TK CROSS VS KUMO STRENGHT
# #Get price on tkcross
# price_list = z['close']
# price_on_cross =(price_list.iloc[-index])
# print(price_on_cross)

# #Get kumo on tkcross

# #SENKOU SPAN A 
# senkou_span_a = (tenkan_sen+kijun_sen)/2
# print("Senkou span a: ",(senkou_span_a))
# #ichi_values.append(senkou_span_a)

# #SENKOU SPAN B 
# ssbh = float(candle_h[-52:].max())
# ssbl = float(candle_l[-52:].min())
# senkou_span_b = (ssbh+ssbl)/2
# print("Senkou span b: ",(senkou_span_b))
# #ichi_values.append(senkou_span_b)
