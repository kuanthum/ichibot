
from token_select import token, side_s, bal, sl, tp
#from set_margin_lev import *

sym = token()

# get_position = session.my_position(sym)['result']
# print(set_margin(sym))
# print(set_lev(sym))


# Auto Market Order Config
def auto_order_d_func():
    order_values = [
        sym[0],
        side_s(),
        "Market",
        bal,
        "GoodTillCancel",
        False,
        False,
        sl,
        tp
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

if __name__ == "__main__":
    auto_order_d_func()

