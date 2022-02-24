import pandas as pd

from pybit import HTTP

session = HTTP("https://api-testnet.bybit.com")

respuesta = session.query_symbol()['result']

df1 = pd.DataFrame(respuesta)

symbol = df1['name']

symbols = list(symbol)

print(symbols)