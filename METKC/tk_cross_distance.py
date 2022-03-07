
from pruebadefunciones.api_pybit import sym_data
import pruebadefunciones.config as cfg
from pruebadefunciones.fr_time import f_time_func
#get symbol data
#for example AVAXUSDT



sym_value_list = ['AVAXUSDT','D', f_time_func()]
sym_keys_list = ['symbol','interval','from_time']
qki = cfg.symbol_data_func(sym_value_list, sym_keys_list)
sym_data(qki)

print(sym_data())