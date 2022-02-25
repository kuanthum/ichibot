import pandas as pd
import fr_time as t
from pybit import HTTP

#conection
session = HTTP("https://api-testnet.bybit.com",
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)

print("")
print("---Logged in---")
print("") 

#get simbols
rsymbols = session.query_symbol()['result']
df1 = pd.DataFrame(rsymbols)
symbol = df1['name']
symbols = list(symbol)

#get_sym_data
sym_data = session.query_kline(symbol='BTCUSDT',interval='D',from_time=t.f_time)['result']
get_sym_data = pd.DataFrame(sym_data)

#get_wallet_balance
balance = session.get_wallet_balance(coin="USDT")['result']
df2 = pd.DataFrame(balance)

#get_server_time
server_time = session.server_time()['time_now']
