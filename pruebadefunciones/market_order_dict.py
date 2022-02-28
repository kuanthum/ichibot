from auto_pos import auto_values

#get values and keys for create dict to place order in "market order module"

order_values = auto_values
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



