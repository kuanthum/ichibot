from api_pybit import sym_data, q_kline
from ichi_data import ichi_var
from ichi_test import ichi_test_func 
from filter_sorted import btc_parallel_trend
from BTCm15 import btc_trend

print(" ")
print("Runing Ichimoku on m1...")
print(" ")

filtered_list = btc_parallel_trend()
sorted_rank = []

interval = 1
days = 0.135

def sym_data_iter_func():
    sym_data_list = []
    for s in filtered_list:
        symbol_data = q_kline(s[0],interval,days)
        sym_data_list.append(symbol_data)
        #print(symbol_data)
    return sym_data_list 

if __name__ == "__main__":

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
            print(f"\rScore: {asset_rank}   ", end = " ")
            sim_rank.append(asset_rank)
    return sim_rank

if __name__ == "__main__":
    ranked_list = asset_rank()
    #Ordenar lista por puntaje
    sorted_rank = sorted(ranked_list, key = lambda symbol : symbol [1])
    print(sorted_rank)
    m1_list = []

btc_trending = btc_trend()

if btc_trending[1] > 0:
    for i in sorted_rank:
        if i[1] == 4:
            m1_list.append(i)
elif btc_trending[1] < 0:
    for i in sorted_rank:
        if i[1] == -4:
            m1_list.append(i)

print("")
print(m1_list)
print("---")