#More efective tk cross
#example on AVAXUSDT

from api_pybit import sym_data, q_kline
#from assetlisttest import sorted_list_test
from filter_sorted import filtered_list

interval = 1
days = 0.135

for i in filtered_list:

    s = i[0]
    print("------")
    print("METKC for :",s)
    print("------")
    q_kline_response = q_kline(s,interval,days)
    z = sym_data(q_kline_response)
    tk_n = i[2]

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
        
        #TENKAN-SEN (convertion line)
        thigh = float(candle_h[c:last_c].max())
        tlow = float(candle_l[c:last_c].min())
        tenkan_sen = (thigh+tlow)/2

        #KIJUN-SEN (base line) 
        khigh = float(candle_h[c2:last_c].max())
        klow = float(candle_l[c2:last_c].min())
        kijun_sen = (khigh+klow)/2

        c = (c-1)
        c2 = (c2-1)
        last_c -= 1

        if tenkan_sen >= kijun_sen:
            tk_cross = 1
        else:
            tk_cross = -1    

        index += 1
        
    print('while stop ------------------------------------')

    tkc_distance = (index-1)
    print("TKcross distance is: ", index-1)
    price_on_tkc = (z['close'].iloc[-index])
    tkc_vs_price = ((tenkan_sen + kijun_sen)/2)

    #TK CROSS STRENGH ANALIZER
    #print(tk_n)

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
    TKCSA()

    print("=================================================================")
   