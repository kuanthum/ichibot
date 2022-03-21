#from iterator import sorted_rank
from api_pybit import df2
from dataframetokens import strenght_sort
#Get token and score to trade

#['Symbol','Price','Ichi Score', 'Distance to tk cross', 'Tk cross strength']
def token():

    token = strenght_sort[0]
    return token

#Get token symbol
token_s = token()
symbol = token_s[0]

#Get order cost from balance
balsheet = df2['USDT']
bal = int(balsheet.iloc[0])

#price
price_now = token_s[1]

lev = 5
#Get qty
qty = (bal*lev/price_now)
#(bal/precio)*bal


#Get side
token_s = token()
def side_s():
    if token_s[2] < 0:
        side = "Sell"
    else:
        side = "Buy"
    return side
print(side_s())




#Get tp/sp anchored
stop_l = 1
take_p = 2
per_sl = price_now*float(stop_l)/100
per_tp = price_now*float(take_p)/100


def risk_mgmt():
    if side_s() == "Sell":
        stop_price = (price_now + per_sl)
        profit_price = (price_now - per_tp)
        risk_mgmt_l = [stop_price, profit_price]
        return risk_mgmt_l
    else:
        stop_price = (price_now - per_sl)
        profit_price = (price_now + per_tp)
        risk_mgmt_l = [stop_price, profit_price]
        return risk_mgmt_l

risk_mgmt_list = risk_mgmt()
sl = round(risk_mgmt_list[0], 5)
tp = round(risk_mgmt_list[1], 5)

print(symbol)
print(price_now)
# print(per_sl)
# print(per_tp)
# print(risk_mgmt())
print(sl,tp)
print(qty)