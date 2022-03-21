
import api_pybit as gd
import pandas as pd
from autoconfig import auto_order_d_func


#get dictionary for inject to request
market_order_dict = auto_order_d_func()

def market_order():
    market_order = (gd.session.place_active_order(**market_order_dict))
    #organaize response
    md_dataframe = pd.DataFrame(market_order)['result']
    return md_dataframe

if __name__ == "__main__":
    print(market_order())
