from api_pybit import session
import pandas as pd
from token_select import token

#token = ['MASKUSDT', 4.41, -4, 0, 'strong']

sym = token()
print(sym[0])

get_lev_marg = session.my_position(
    symbol = sym[0]
)['result']

df = pd.DataFrame(get_lev_marg)
df_margin = df['is_isolated']
df_lev = df['leverage']


if df_margin.iloc[0] == True:
    print(df['is_isolated'])
    if df_lev.iloc[0] != 5:
        print("Setting lev on 5")
        session.set_leverage(
        symbol=sym[0],
        buy_leverage=5,
        sell_leverage=5
        )
    else:
        print("Everything ok")

else:
    print("Switching to isolated and seting lev to 5")
    session.cross_isolated_margin_switch(
    symbol=sym[0],
    is_isolated=True,
    buy_leverage=5,
    sell_leverage=5
)
    

