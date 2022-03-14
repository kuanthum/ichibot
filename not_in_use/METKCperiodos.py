
#More efective tk cross
#example on AVAXUSDT

from api_pybit import sym_data, q_kline
from ichi_data import ichi_var
from ichi_test import ichi_test_func

s = "EOSUSDT"
interval = 1
days = 0.0135
q_kline(s,interval,days)

z = sym_data(q_kline)
x = ichi_var(z)
tk_n = ichi_test_func(**x)[3]

symbol = z['symbol']
candle_c = z['close']
candle_h = z['high']
candle_l = z['low']
lastprice = float(candle_c.iloc[-1])

c = -9
c2 = -26
last_c = len(z)
index = 0
tk_cross = tk_n

while tk_cross == tk_n:
    print('---------- Iteracion: ',index)
    print(c, c2)
    print(last_c)
    print('precio de cierre: ', z['close'].iloc[last_c-1])
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

tkc_distance = (index-1)
print(index-1)
price_on_tkc = (z['close'].iloc[-index])
print(z['close'].iloc[-index])
tkc_vs_price = ((tenkan_sen + kijun_sen)/2)
print((tenkan_sen + kijun_sen)/2)

#TK CROSS STRENGH ANALIZER
print(tk_n)

tk_strength = ()

def TKCSA():
    while True:
        if tk_n == -1 and price_on_tkc < tkc_vs_price:
            print('tkcross is: strong')
            tk_strength = -1
        elif tk_n == -1 and price_on_tkc > tkc_vs_price:
            print('tkcross is weak')
            tk_strength = 0
        elif tk_n == 1 and price_on_tkc > tkc_vs_price:
            print('tkcross is strong')
            tk_strength = 1
        else:
            print('tkcross is weak')
            tk_strength = 0
        return tk_strength

print(TKCSA())