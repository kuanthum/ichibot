
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
#print(type(z))
#print(z)
x = ichi_var(z)
#print(type(x))
#print(x)
tk_n = ichi_test_func(**x)[3]
#print(tk_cross)

c = -9
c2 = -26
index = 0
tk_cross = tk_n

while tk_cross == tk_n:

    ichi_values = []
    symbol = z['symbol']
    #ichi_values.append(symbol[1])
    candle_c = z['close']
    candle_h = z['high']
    candle_l = z['low']
    #lastprice = float(candle_c.iloc[-1])
    #ichi_values.append(lastprice)
    #print(symbol[1])
    #print("Lastprice: ",(lastprice))

    #TENKAN-SEN (convertion line)
    thigh = float(candle_h[c:].max())
    tlow = float(candle_l[c:].min())
    tenkan_sen = (thigh+tlow)/2
    #print("Tenkan sen: ", tenkan_sen)

    #KIJUN-SEN (base line) 
    khigh = float(candle_h[c2:].max())
    klow = float(candle_l[c2:].min())
    kijun_sen = (khigh+klow)/2
    #print("Kijun sen: ",kijun_sen)

    c = (c-1)
    c2 = (c2-1)

    #print(c, c2)

    if tenkan_sen >= kijun_sen:
        tk_cross = 1
    else:
        tk_cross = -1    

    index += 1

print(index)


