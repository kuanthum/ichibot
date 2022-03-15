
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

print(auto_order_d_func())

#Query klyne config


