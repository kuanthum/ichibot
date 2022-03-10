from ichi_data import ichi_var
from ichi_test import ichi_test_func
from api_pybit import sym_data, q_kline


def btc_trend():
    s = 'BTCUSDT'
    interval = 15
    days = 1

    qky = q_kline(s,interval,days)
    var = sym_data(qky)
    data = ichi_var(var)
    btc_tendence = ichi_test_func(**data)
    return btc_tendence


#print(btc_trend())