import get_data as gd

candle_c = gd.get_sym_data['close']
candle_h = gd.get_sym_data['high']
candle_l = gd.get_sym_data['low']
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


