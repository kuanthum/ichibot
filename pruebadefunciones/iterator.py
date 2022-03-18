from api_pybit import symbols, sym_data, q_kline
from ichi_data import ichi_var
from ichi_test import ichi_test_func

print(" ")
print("Runing Ichimoku on m5...")
print(" ")

sorted_rank = []

# interval = 1
# days = 0.135
days = 0.65
interval = '5'

def sym_data_iter_func():
    sym_data_list = []
    for s in symbols():
        symbol_data = q_kline(s,interval,days)
        sym_data_list.append(symbol_data)
    return sym_data_list 

sym_entry_list = sym_data_iter_func()
sym_entry_list = sym_entry_list[6:-6]

def asset_rank():
    sim_rank = []
    for i in sym_entry_list:
        s = sym_data(i)
        if len(s) < 61:
            print("Not suficient data for :", s['symbol'].iloc[1])
        else:
            ichi_var(s)
            dict_for_test = ichi_var(s)
            asset_rank = ichi_test_func(**dict_for_test)
            #print("\r{}".format(s), end =" ")
            print(f"\rScore: {asset_rank}   ", end = " ")
            sim_rank.append(asset_rank)
    return sim_rank

ranked_list = asset_rank()
#Ordenar lista por puntaje
sorted_rank = sorted(ranked_list, key = lambda symbol : symbol [1])
print(sorted_rank)
