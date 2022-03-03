import pandas as pd
from pybit import HTTP
from fr_time import f_time_func
import config as cfg

#conection
session = HTTP("https://api-testnet.bybit.com",
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)

print("")
print("---Logged in---")
print("") 

#get simbols
def symbols():
    rsymbols = session.query_symbol()['result']
    print(rsymbols)
    df1 = pd.DataFrame(rsymbols)
    print(df1)
    symbol = df1['name']
    symbols = list(symbol)
    return symbols
print(symbols())

#get_sym_data

s = ()
sym_value_list = ['BTCUSDT','D', f_time_func()]
sym_keys_list = ['symbol','interval','from_time']
qki = cfg.symbol_data_func(sym_value_list, sym_keys_list)

def sym_data(qki):
    symbol_data_q = session.query_kline(**qki)['result']
    symbol_data = pd.DataFrame(symbol_data_q)
    return symbol_data

print(sym_data(qki))
print(type(sym_data(qki)))

#get_wallet_balance
balance = session.get_wallet_balance(coin="USDT")['result']
df2 = pd.DataFrame(balance)

#get_server_time
server_time = session.server_time()['time_now']

#active order
active_order = session.get_active_order(
    symbol="BTCUSDT",
    side="Buy",
    order_type="Market",
    qty=0.002,
    time_in_force="GoodTillCancel",
    reduce_only= False,
    close_on_trigger= False,
    stop_loss= False,
    take_profit= False
)
