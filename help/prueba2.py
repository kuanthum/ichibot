

list = [['BTCUSDT', 2], ['ETHUSDT', -1], ['EOSUSDT', -4], ['XRPUSDT', 1], ['BCHUSDT', -3], ['LTCUSDT', -4]]

#preguntar Nico
ordenados = sorted(list, key = lambda symbol : symbol [1])

print(ordenados)

