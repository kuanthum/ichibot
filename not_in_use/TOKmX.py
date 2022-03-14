from ichi_data import ichi_var
from ichi_test import ichi_test_func
from api_pybit import sym_data, q_kline


# s = 'AVAXUSDT'
# interval = 1
# days = 0.135

s = 'AVAXUSDT'
interval = 5
days = 0.65


qky = q_kline(s,interval,days)
var = sym_data(qky)
data = ichi_var(var)
tok_trend = ichi_test_func(**data)


print(var)
print(data)
print(tok_trend)
