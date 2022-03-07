
from datetime import datetime
import calendar

#unixtime get for market data
def f_time_func():
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    f_time = unixtime - 60 * 60 * 24*100
    return f_time

#Market Order Config
def auto_order_d_func():
    order_values = [
        "BTCUSDT",
        "Buy",
        "Market",
        0.002,
        "GoodTillCancel",
        False,
        False,
        32000,
        60000
    ]
    order_keys = [
        'symbol',
        'side',
        'order_type',
        'qty',
        'time_in_force',
        'reduce_only',
        'close_on_trigger',
        'stop_loss',
        'take_profit'
    ]
    market_order_d = dict(zip(order_keys, order_values))
    return market_order_d

#print(auto_order_d_func())

#Query klyne config

s = ()
sym_value_list = [s,'D', f_time_func()]
sym_keys_list = ['symbol','interval','from_time']
    
def symbol_data_func(sym_value_list, sym_keys_list):
  
    query_kline_d = dict(zip(sym_keys_list, sym_value_list))
    return query_kline_d

#print(symbol_data_func(sym_value_list, sym_keys_list))

#laverage
# Laverage config
#true for isolated, false for
laverage_value_list = ["BTCUSDT",True,10,20]
laverage_keys_list = ['symbol','is_isolated','buy_laverage','sell_laverage']
set_laverage_dict = dict(zip(laverage_keys_list,laverage_value_list))