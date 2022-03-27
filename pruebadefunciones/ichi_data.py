
#Recibe DataFrame y en segunda fase tk_n 
def ichi_var(var,tk_n):
 
    ichi_values = []
    ichi_keys = [
        'symbol',
        'lastprice',
        'tenkan_sen',
        'kijun_sen',
        'senkou_span_a',
        'senkou_span_b',
        'senkou_span_a_now',
        'senkou_span_b_now',
        'chikou'
    ]

    pandas_data = (var)

    #Definimos variables num'ericas
    c = 9
    c2 = 26
    c3 = 52
    last_c = None
    #last_c = len(pandas_data)
    #tk_cross = tk_n

    #get specific data form sym data
    symbol = pandas_data['symbol']
    candle_c = pandas_data['close']
    candle_h = pandas_data['high']
    candle_l = pandas_data['low']
    lastprice = float(candle_c.iloc[-1])

    #----ICHIMOKU DATA----

    #TENKAN-SEN (convertion line)
    def tenkan_sen(candle_h,c,last_c,candle_l):
        thigh = float(candle_h[-c:last_c].max())
        tlow = float(candle_l[-c:last_c].min())
        tenkan_sen = (thigh+tlow)/2
        return tenkan_sen
    #print("Tenkan sen: ", tenkan_sen)
   
    #KIJUN-SEN (base line)
    def kijun_sen(candle_h,c2,last_c,candle_l): 
        khigh = float(candle_h[-c2:last_c].max())
        klow = float(candle_l[-c2:last_c].min())
        kijun_sen = (khigh+klow)/2
        return kijun_sen
        #print("Kijun sen: ",kijun_sen)
    
    if tk_n != 0:
        def tk_distance(symbol,c,c2):
            tk_cross = tk_n
            last_c = len(pandas_data)
            index = 0
            while tk_cross == tk_n:
                
                c = (c+1)
                c2 = (c2+1)
                last_c -= 1
                tenkan_s = tenkan_sen(candle_h,c,last_c,candle_l)
                kijun_s = kijun_sen(candle_h,c2,last_c,candle_l)

                if tenkan_s >= kijun_s:
                    tk_cross = 1
                else:
                    tk_cross = -1
                index += 1

            tkc_distance = (index-1)
            price_on_tkc = (pandas_data['close'].iloc[-index])
            tkc_vs_price = ((tenkan_s + kijun_s)/2)
            result = [symbol[1], tk_n, price_on_tkc, tkc_vs_price,tkc_distance]

            #print("Tkcross distance is: ", tkc_distance)

            return result
        print("TkC distance function:... ", tk_distance(symbol,c,c2))
        return tk_distance(symbol,c,c2)
    else: pass

    tenkan_s = tenkan_sen(candle_h,c,last_c,candle_l)
    kijun_s = kijun_sen(candle_h,c2,last_c,candle_l)

    #TENKAN LOOKBACK
    thigh26 = float(candle_h[-c-c2:-c2].max())
    tlow26 = float(candle_l[-c-c2:-c2].min())
    tenkan_sen_26 = (thigh26+tlow26)/2
    #print("Tenkan sen look back: ", tenkan_sen_26)
    #ichi_values.append(tenkan_sen_26)
   
    #KIJUN LOOKBACK
    khigh = float(candle_h[-c2-c2:-c2].max())
    klow = float(candle_l[-c2-c2:-c2].min())
    kijun_sen_26 = (khigh+klow)/2
    #print("Kijun sen lookback: ",kijun_sen_26)
    #ichi_values.append(kijun_sen_26)

    ichi_values.append(symbol[1])
    ichi_values.append(lastprice)
    ichi_values.append(tenkan_s)
    ichi_values.append(kijun_s)
    #----KUMO CLOUD----

    #KUMO AHEAD

    #SENKOU SPAN A 
    senkou_span_a = (tenkan_s+kijun_s)/2
    #print("Senkou span a: ",(senkou_span_a))
    ichi_values.append(senkou_span_a)

    #SENKOU SPAN B 
    ssbh = float(candle_h[-c3:].max())
    ssbl = float(candle_l[-c3:].min())
    senkou_span_b = (ssbh+ssbl)/2
    #print("Senkou span b: ",(senkou_span_b))
    ichi_values.append(senkou_span_b)

    #KUMONOW

    #NOWsenkouA
    senkou_span_a_now = (tenkan_sen_26+kijun_sen_26)/2
    #print("Senkou span a lookback: ",(senkou_span_a_now))
    ichi_values.append(senkou_span_a_now)

    #NOWsenkowB
    ssbh1 = float(candle_h[-c3-c2:-c2].max())
    ssbl1 = float(candle_l[-c3-c2:-c2].min())
    senkou_span_b_now = (ssbh1+ssbl1)/2
    #print("Senkou span b lookback: ",(senkou_span_b_now))
    ichi_values.append(senkou_span_b_now)

    #Chikou
    chikou = float(candle_c.iloc[-c2])
    ichi_values.append(chikou)

    #print(" ")
    #print("------------------------------------------------------------------------")
    #print(" ")

    result = dict(zip(ichi_keys, ichi_values))
    ##print(ichi_test_inputs)

    return result

if __name__ == "__main__":
    ichi_var()


