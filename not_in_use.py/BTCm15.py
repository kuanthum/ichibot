from ichi_data import ichi_var
from ichi_test import ichi_test_func
from api_pybit import sym_data, q_kline


#GET_BTC_TREND
def btc_trend():
    s = 'BTCUSDT'
    interval = 15
    days = 1

    qky = q_kline(s,interval,days)
    var = sym_data(qky)
    data = ichi_var(var)
    btc_tendence = ichi_test_func(**data)
    return btc_tendence

if __name__ == "__main__":
     print(btc_trend())