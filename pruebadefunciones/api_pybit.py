import pandas as pd
from pybit import HTTP
from datetime import datetime
import calendar

#unixtime get for market data
days = 100
def f_time_func(days):
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.timetuple())
    f_time = unixtime - 60 * 60 * 24*days
    return f_time

#conection
session = HTTP("https://api-testnet.bybit.com",
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)

print("")
print("---Logged in---")
print("") 

#1get simbols
def get_symbols():
    rsymbols = session.query_symbol()['result']
    df1 = pd.DataFrame(rsymbols)
    symbol = df1['name']
    symbols = list(symbol)
    return symbols

if __name__ == "__main__":
    get_symbols()

#2get_sym_data
days = 100
sym = 'BTCUSDT'
interval = 'D'

#EMPAQUETA INPUTS PARA GENERAR DICCIONARIO
def get_q_kline(sym,interval,days):
    sym_value_list = [sym,interval, f_time_func(days)]
    sym_keys_list = ['symbol','interval','from_time']
    qk_list = [sym_keys_list, sym_value_list]
    query_kline_d = dict(zip(*qk_list))
    return query_kline_d

if __name__ == "__main__":
    get_q_kline()

##### REVISAR ESTO
qkd = get_q_kline(sym,interval,days)

#PIDE DATA DEL MERCADO A PARTIR DE UN DICCIONARIO
def get_sym_data(qkd):
    symbol_data_q = session.query_kline(**qkd)['result']
    symbol_data = pd.DataFrame(symbol_data_q)
    return symbol_data

if __name__ == "__main__":
    get_sym_data()

#4get_wallet_balance
def get_balance ():
    balance = session.get_wallet_balance(coin="USDT")['result']
    df2 = pd.DataFrame(balance)
    return df2

if __name__ == "__main__":
    get_balance()


#5get_server_time
def get_server_time():
    server_time = session.server_time()['time_now']
    return server_time

if __name__ == "__main__":
    get_server_time()

#7get position
def get_pos():
    response = session.my_position("/private/linear/position/list")['result']

    data_list = []
    for i in response:
        data_list.append(i['data'])

    pos_df = pd.DataFrame(data_list)
    df = pos_df[['symbol','position_value']]
    return df

#ACOMODAR ESTO... ESTO ES PARA SABER SI HAY POSICIONES ABIERTAS
# index = 0
# for i in df['position_value']:
#     index += 1
#     if i != 0:
#         print(df.loc[index-1])
#         return df.loc[index-1]

#7 OBTENER LISTA de DICCIONARIOS, DONDE CADA INDICE CONTIENE OBJETO CON EL SIGUIENTE FORMATO
#{'symbol': 'BTCUSD', 'interval': '5', 'from_time': 1647953837.0}

#6active order
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

def get_sym_data_list (symbols, interval, days, start, to):

    sym_data_list = []
    for s in symbols:
        symbol_data = get_q_kline(s,interval,days)
        sym_data_list.append(symbol_data)

    #OJO CON ESTO CUANDO SE REPITA
    sym_entry_list = sym_data_list[start:to]
    return sym_entry_list

if __name__ == "__main__":
    get_sym_data_list()
    
#sym_entry_list = get_sym_data_list(symbols, interval, days)

#GENERAR LIBRO CON DATAFRAMES PARA ANALIZAR EN ICHIMOKU
def market_data_book(sym_entry_list):
    market_data_book_list = []
    for i in sym_entry_list:
        sym_data = get_sym_data(i)
        print(f"\rScore: {sym_data}       ", end = " ")
        market_data_book_list.append(sym_data)
    return market_data_book_list

#generar lista de simbolos a partir de listas filtradas por ichimoku
def new_symbols(filtered_list):
    symbols = []
    for i in filtered_list:
        symbols.append(i[0])
    return symbols
