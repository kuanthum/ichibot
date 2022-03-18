import pandas as pd
from pybit import HTTP

#conection
session = HTTP("https://api-testnet.bybit.com",
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)
print("---")
print("logged")
print("---")

get_position = session.my_position("/private/linear/position/list")['result']
#get_pos = pd.DataFrame(get_position)
print(get_position)

new_list = list()

for i in get_position:
    new_list.append(i['data'])

pos_df = pd.DataFrame(new_list)
df = pos_df[['symbol','position_value']]
#agregar is_isolated, buy_leverage, sell_leverage

def get_pos():
    index = 0
    for i in df['position_value']:
        index += 1
        if i != 0:
            print(df.loc[index-1])
            return df.loc[index-1]

print(get_pos())