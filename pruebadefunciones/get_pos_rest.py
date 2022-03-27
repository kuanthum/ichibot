import pandas as pd
from api_pybit import get_pos

new_list = list()

for i in get_pos():
    new_list.append(i['data'])

pos_df = pd.DataFrame(new_list)
df = pos_df[['symbol','position_value']]
#agregar is_isolated, buy_leverage, sell_leverage

def look_for_position():
    index = 0
    for i in df['position_value']:
        index += 1
        if i != 0:
            print(df.loc[index-1])
            return df.loc[index-1]

print(get_pos())