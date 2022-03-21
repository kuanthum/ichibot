import pandas as pd
from pybit import HTTP
from fr_time import f_time_func
#import config as cfg

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
    df1 = pd.DataFrame(rsymbols)
    symbol = df1['name']
    symbols = list(symbol)
    print(symbol)
    return symbols

if __name__ == "__main__":
    symbols()

#get_sym_data
 
days = 100
s = 'BTCUSDT'
interval = 'D'

def q_kline(s,interval,days):
    sym_value_list = [s,interval, f_time_func(days)]
    sym_keys_list = ['symbol','interval','from_time']
    qk_list = [sym_keys_list, sym_value_list]
    query_kline_d = dict(zip(*qk_list))
    print('q_kline')
    return query_kline_d

    #default dict
if __name__ == "__main__":
    qkd = q_kline(s,interval,days)

def sym_data(qkd):
    symbol_data_q = session.query_kline(**qkd)['result']
    symbol_data = pd.DataFrame(symbol_data_q)
    return symbol_data

if __name__ == "__main__":
    sym_data(qkd)

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

# #get price index
# def bifpa(s):
#     session.latest_information_for_symbol(
#     symbol=s
# )



#set laverage

if __name__ == "__main__":
    symbols()
    q_kline()
    sym_data()