from api_pybit import get_symbols, get_sym_data, get_q_kline
from ichi_data import ichi_var
from ichi_test import ichi_test_func

print(" ")
print("Runing Ichimoku on m5...")
print(" ")

days = 0.65
interval = '5'

def iterador_m5():

    sym_data_list = []

    for s in get_symbols():
        symbol_data = get_q_kline(s,interval,days)
        sym_data_list.append(symbol_data)

    sym_entry_list = sym_data_list[8:-6]

    sym_rank = []

    for i in sym_entry_list:
        s = get_sym_data(i)
        ichi_var(s)
        dict_for_test = ichi_var(s)
        asset_rank = ichi_test_func(**dict_for_test)
        print(f"\rScore: {asset_rank}       ", end = " ")
        sym_rank.append(asset_rank)
    
    #Ordenar lista por puntaje
    sorted_rank = sorted(sym_rank, key = lambda symbol : symbol [1])

    return sorted_rank

if __name__ == "__main__":
    iterador_m5()