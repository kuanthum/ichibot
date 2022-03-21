#importar lista
from iterator import sorted_rank
from BTCm15 import btc_trend

print("")
print("Getting BTC trend and filtering parallel assets...")
print("")

# sorted_rank = [
#     ['EOSUSDT', -4, 1.950],
#     ['BCHUSDT', -4, 300.7],
#     ['LTCUSDT', -3, 104.88],
#     ['XTZUSDT', 1, 3.199],
#     ['LINKUSDT', 2, 14.136],
#     ['ADAUSDT', 0, 0.8764],
#     ['DOTUSDT', 3, 17.17]
# ]

btc_t = btc_trend()
asset_list = sorted_rank
print("")
print('----')
print("BTC trend: ", btc_t[1])
print('----')
print("")

#eleminar todos los valores que no coincidan con la tendencia de btc
def btc_parallel_trend():
    while True:
        new_list = []
        if btc_t[1] < 0:
            for i in sorted_rank:
                if i[1] == -4:
                    new_list.append(i)
        elif btc_t[1] > 0:
            for i in sorted_rank:
                if i[1] == 4:
                    new_list.append(i)
        return new_list

if __name__ == "__main__":
    print(btc_parallel_trend())
    #filtered_list = (btc_parallel_trend())
