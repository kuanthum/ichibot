#from iterator import sorted_rank
from api_pybit import df2

#Get token and score to trade
def token():
    sorted_ranking = [
        ['EOSUSDT', -4],
        ['BCHUSDT', -4],
        ['LTCUSDT', -4],
        ['XTZUSDT', -4],
        ['LINKUSDT', -4]
    ]
    token = sorted_ranking[0]
    return token

#Get token symbol
token_s = token()
token_d = token_s[0]

#Get qty from balance
balsheet = df2['USDT']
bal = int(balsheet.iloc[0])

#Get side
token_s = token()
def side_s():
    if token_s[1] < 0:
        side = "Sell"
    else:
        side = "Buy"
    return side    