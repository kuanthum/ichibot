
import get_data as gd
import pandas as pd
import market_order_dict as md


#get dictionary for inject to request
market_order_dict = md.market_order_d

market_order = (gd.session.place_active_order(**market_order_dict))

#organaize response
md_dataframe = pd.DataFrame(market_order)['result']
print(md_dataframe)


