
from tokenselectfortrading import token_d, side_s, bal


# Auto Market Order Config
def auto_order_d_func():
    order_values = [
        token_d,
        side_s(),
        "Market",
        bal,
        "GoodTillCancel",
        False,
        False,
        5,
        1
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

