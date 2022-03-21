from get_pos_rest import get_pos
from auto_market_order import market_order
from BTCm15 import btc_trend

btc_t = btc_trend()

while True:
    if get_pos() == None:
        if btc_t[1] != 0:
            print('BTC is trending')
            #print("\rAnalizing to trade...", end = '')
            print(market_order())
        else: #wait
            print("BTC is not trending...")
    else:
        print("There is already a position open: ", get_pos())


