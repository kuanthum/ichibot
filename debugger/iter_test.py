
from fr_time import f_time_func
from api_pybit import symbols, sym_data
import config as cfg
from ichi_data import ichi_var
from ichi_test import ichi_test_func
from fr_time import candle_data

def sym_data_iter_func():
    sym_data_list = []
    for s in symbols():
        svl = [s,'D', f_time_func()]
        skl = ['symbol','interval','from_time']
        symbol_data = cfg.symbol_data_func(svl, skl)
        sym_data_list.append(symbol_data)
    return sym_data_list 

sym_entry_list = sym_data_iter_func()
sym_entry_list = sym_entry_list[0:]

def asset_rank():
    sim_rank = []
    for i in sym_entry_list:
        s = sym_data(i)
        ichi_var(s)
        dict_for_test = ichi_var(s)
        asset_rank = ichi_test_func(**dict_for_test)
        sim_rank.append(asset_rank)
    return sim_rank

ranked_list = asset_rank()
sorted_rank = sorted(ranked_list, key = lambda symbol : symbol [1])
print(sorted_rank)
