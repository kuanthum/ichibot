#from iterator import sorted_rank
from api_pybit import df2

#Get token and score to trade
def token():
    sorted_ranking = [
    ['EOSUSDT', -4, 1.950],
    ['BCHUSDT', -4, 300.7],
    ['LTCUSDT', -4, 104.88],
    ['XTZUSDT', -4, 3.199],
    ['LINKUSDT', -4, 14.136],
    ['ADAUSDT', -4, 0.8764],
    ['DOTUSDT', -4, 17.17]
    ]
    token = sorted_ranking[0]
    return token

#Get token symbol
token_s = token()
token_d = token_s[0]

#Get order cost from balance
balsheet = df2['USDT']
bal = int(balsheet.iloc[0])

#price
price_now = token_s[2]

#Get qty
qty = (bal/price_now)
#(bal/precio)*bal


#Get side
token_s = token()
def side_s():
    if token_s[1] < 0:
        side = "Sell"
    else:
        side = "Buy"
    return side
#print(side_s())




#Get tp/sp anchored
stop_l = 5
take_p = 10
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
sl = round(risk_mgmt_list[0], 3)
tp = round(risk_mgmt_list[1], 3)

# print(price_now)
# print(per_sl)
# print(per_tp)
# print(risk_mgmt())
print(sl,tp)
print(qty)