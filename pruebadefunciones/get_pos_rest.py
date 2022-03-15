import pandas as pd
import json
from pybit import HTTP


#conection
session = HTTP("https://api-testnet.bybit.com/private/linear/position/list",
    api_key="WJYwnYE2Qv6XUrEMwW",
    api_secret="AVR49x1rNyn98xMdqjtXxl5jWtxROnSlpZs2"
)
print("---")
print("logged")
print("---")


get_position = json.load(session.my_position(symbol=""))
# #get_position = pd.DataFrame(get_position)

# print(get_position)
