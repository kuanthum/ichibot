from ichi_data import *



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
