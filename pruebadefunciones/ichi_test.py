
def ichi_test_func(
    symbol= (),
    lastprice= (),
    tenkan_sen= (),
    kijun_sen= (),
    senkou_span_a= (),
    senkou_span_b= (),
    senkou_span_a_now= (),
    senkou_span_b_now= (),
    chikou= ()
):

    def tk_cross():
        if tenkan_sen > kijun_sen:
            return 1 
        else:
            return -1    

    #print("TK cross is: ",tk_cross())

    #KUMO AHEAD
    def kumo_cloud():
        if senkou_span_a > senkou_span_b:
            return 1
        else:
            return -1

    #print("Kumo ahead is: ",kumo_cloud())

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

    #print("Price vs Kumo is: ",kumo_cloud_now())

    #CHIKOU
    def chikou_test():
        if lastprice > chikou:
            return 1
        else:
            return -1


    #print("Chikou is: ",chikou_test())

    #print(" ")
    #print("------------------------------------------------------------------------")
    #print(" ")


    puntaje = (tk_cross() + kumo_cloud() + kumo_cloud_now() + chikou_test())
    rank = [symbol, puntaje, lastprice]

    #print(rank)

    def commend():
        if puntaje == 4:
            return "go LONG"
        elif puntaje == -4:
            return "go SHORT"
        else:
            return "go SLEEP"

    #print("Recomendacion: ",commend())

    #print(" ")
    #print("------------------------------------------------------------------------")
    #print(" ")
    return rank
