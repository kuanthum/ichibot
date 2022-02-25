import get_data as gd
import pandas as pd
from open_pos_q import *
from open_pos_a import open_pos_auto
from stop_profit_calc import *
from pruebadefunciones.main import mode_select

if mode_select.lower() == "m":
    open_pos_input()
else:
    open_pos_auto()

market_order = (gd.session.place_active_order(
    symbol="BTCUSDT",
    side= direction_p,
    order_type="Market",
    qty=0.002,
    time_in_force="GoodTillCancel",
    reduce_only = False,
    close_on_trigger = False,
    stop_loss = sl,
    take_profit = tp
))

md_dataframe = pd.DataFrame(market_order)['result']
print(md_dataframe)

