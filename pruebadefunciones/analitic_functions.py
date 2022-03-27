import ichi_data as id
import ichi_test as it


#7 OBTENER LISTA de DICCIONARIOS, 
def ichimoku(market_book,phase):

    #automatizar intervalo a d[ias]
    print("Runing Ichimoku...")
    
    sym_rank = []
    tk_cross_list = []

    for i in market_book:

        dict_for_test = id.ichi_var(i,phase)
        if phase != 0:
            tk_cross_list.append(dict_for_test)
        else:
            asset_rank = it.ichi_test_func(**dict_for_test)
            #print(f"\rScore: {asset_rank}       ", end = " ")
            sym_rank.append(asset_rank)

    if phase != 0:
        return tk_cross_list
    else:
        sorted_rank = sorted(sym_rank, key = lambda symbol : symbol [1])
        return sorted_rank

if __name__ == "__main__":
    print(ichimoku())

#eleminar todos los valores que no coincidan con la tendencia de btc
def btc_parallel_filter(sorted_rank, btc_trend):

    while True:
        btc_parallel = []
        if btc_trend[1] < 0:
            for i in sorted_rank:
                if i[1] == -4:
                    btc_parallel.append(i)
        elif btc_trend[1] > 0:
            for i in sorted_rank:
                if i[1] == 4:
                    btc_parallel.append(i)
        else:
            btc_parallel = 'Btc is not trending'
        return btc_parallel

if __name__ == "__main__":
    print(btc_parallel_filter())

#Tkc Streght analisis a partir de la data de ichimoku phase 2

def TKCSA(symbol,tk_n, price_on_tkc, tkc_vs_price,tkc_distance):

    while True:
        if tk_n == -1 and price_on_tkc < tkc_vs_price:
            print('tkcross is: strong')
            tk_strength = 1
        elif tk_n == -1 and price_on_tkc > tkc_vs_price:
            print('tkcross is weak')
            tk_strength = 0
        elif tk_n == 1 and price_on_tkc > tkc_vs_price:
            print('tkcross is strong')
            tk_strength = 1
        else:
            print('tkcross is weak')
            tk_strength = 0

        result = [symbol,tk_strength, tkc_distance]
        print(result)
        return result










