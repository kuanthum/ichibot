import get_data as gd
from open_pos_q import *

open_pos_input()

price_now = float(gd.get_sym_data['close'][-1:])
porcentaje_sl = price_now*float(stop_l)/100
porcentaje_tp = price_now*float(take_p)/100

if direction_p == "Buy":
    if sl == 'n':
        sl = False
    else: sl = (price_now - porcentaje_sl) 

    if tp == 'n':
        tp = False
    else: tp = (price_now + porcentaje_tp)
else:
    if sl == 'n':
        sl = False
    else: sl = (price_now + porcentaje_sl) 

    if tp == 'n':
        tp = False
    else: tp = (price_now - porcentaje_tp)