


def ichi_var(var):

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

    #get specific data form sym data
    symbol = pandas_data['symbol']
    ichi_values.append(symbol[1])
    candle_c = pandas_data['close']
    candle_h = pandas_data['high']
    candle_l = pandas_data['low']
    lastprice = float(candle_c.iloc[-1])
    ichi_values.append(lastprice)
    #print(symbol[1])
    #print("Lastprice: ",(lastprice))


    #----ICHIMOKU DATA----

    #TENKAN-SEN (convertion line)
    thigh = float(candle_h[-9:].max())
    tlow = float(candle_l[-9:].min())
    tenkan_sen = (thigh+tlow)/2
    #print("Tenkan sen: ", tenkan_sen)
    ichi_values.append(tenkan_sen)

    #TENKAN LOOKBACK
    thigh26 = float(candle_h[-9-26:-26].max())
    tlow26 = float(candle_l[-9-26:-26].min())
    tenkan_sen_26 = (thigh26+tlow26)/2
    #print("Tenkan sen look back: ", tenkan_sen_26)
    #ichi_values.append(tenkan_sen_26)

    #KIJUN-SEN (base line) 
    khigh = float(candle_h[-26:].max())
    klow = float(candle_l[-26:].min())
    kijun_sen = (khigh+klow)/2
    #print("Kijun sen: ",kijun_sen)
    ichi_values.append(kijun_sen)

    #KIJUN LOOKBACK
    khigh = float(candle_h[-26-26:-26].max())
    klow = float(candle_l[-26-26:-26].min())
    kijun_sen_26 = (khigh+klow)/2
    #print("Kijun sen lookback: ",kijun_sen_26)
    #ichi_values.append(kijun_sen_26)

    #----KUMO CLOUD----

    #KUMO AHEAD

    #SENKOU SPAN A 
    senkou_span_a = (tenkan_sen+kijun_sen)/2
    #print("Senkou span a: ",(senkou_span_a))
    ichi_values.append(senkou_span_a)

    #SENKOU SPAN B 
    ssbh = float(candle_h[-52:].max())
    ssbl = float(candle_l[-52:].min())
    senkou_span_b = (ssbh+ssbl)/2
    #print("Senkou span b: ",(senkou_span_b))
    ichi_values.append(senkou_span_b)

    #KUMONOW

    #NOWsenkouA
    senkou_span_a_now = (tenkan_sen_26+kijun_sen_26)/2
    #print("Senkou span a lookback: ",(senkou_span_a_now))
    ichi_values.append(senkou_span_a_now)

    #NOWsenkowB
    ssbh1 = float(candle_h[-52-26:-25].max())
    ssbl1 = float(candle_l[-52-26:-26].min())
    senkou_span_b_now = (ssbh1+ssbl1)/2
    #print("Senkou span b lookback: ",(senkou_span_b_now))
    ichi_values.append(senkou_span_b_now)

    #Chikou
    chikou = float(candle_c.iloc[-26])
    ichi_values.append(chikou)

    #print(" ")
    #print("------------------------------------------------------------------------")
    #print(" ")

    ichi_test_inputs = dict(zip(ichi_keys, ichi_values))
    ##print(ichi_test_inputs)

    return ichi_test_inputs


