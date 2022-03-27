import analitic_functions as af
from api_pybit import *

trading = ()

def test():
    
    #get btc trend
    phase = 0
    qky = get_q_kline('BTCUSDT', 15, 1)
    market_book = [get_sym_data(qky), ]
    btc_t = af.ichimoku(market_book, phase)[0]

    if btc_t[1] == 0:
        result = "BTC is not trending"
        return result
    else:

        while True:

            days = 0.65
            interval = '5'
            symbols = get_symbols()
            start = 8
            to = -6
            phase = 0

            #Analisis m5
            sym_entry_list = get_sym_data_list(symbols, interval, days, start, to)
            market_book = (market_data_book(sym_entry_list))
            ichi_m5 = af.ichimoku(market_book,phase)
            print("m5")
            print(ichi_m5)

            #filter parallel
            filtered_list = af.btc_parallel_filter(ichi_m5, btc_t)
            print("lista filtrada paralelos a btc")
            print(filtered_list)

            #Analisis m1
            days = 0.135
            interval = '1'
            start = None
            to = None
        
            symbols = new_symbols(filtered_list)
            sym_entry_list = get_sym_data_list(symbols, interval, days, start, to)
            market_book = (market_data_book(sym_entry_list))
            ichi_m1 = af.ichimoku(market_book, phase)

            #ELIMINAR DE LA LISTA LOS QUE NO ESTEN AL PALO
            ichi_filtered = []
            if btc_t[1] > 0:
                z = True

            for i in ichi_m1:
                value = i[1]
                if z == True and value == 4:
                    ichi_filtered.append(i)
                elif z == False and value == -4:
                    ichi_filtered.append(i)


            print("Analisis ichimoku en m1")
            print(ichi_filtered)

            #get METKC, ditance to tkcross, price on that distance 
            print("preparing metck")
            
            filtered = new_symbols(ichi_filtered)
            market_book_filtered = []
            for i in market_book:
                z = i.iloc[1]['symbol']  
                if z in filtered:
                    market_book_filtered.append(i)

            tk_n = ichi_filtered[0]
            phase = tk_n[2]
            tk_cross_list = af.ichimoku(market_book_filtered,phase)

            print("tk_distance")
            print(tk_cross_list)

            def new_list():
                new_list = []
                for i in tk_cross_list:
                    z = af.TKCSA(*i)
                    if z[1] == 1:
                        new_list.append(af.TKCSA(*i))
                return new_list

            new_list_result = new_list()
            print("Strenght list compacter")

            #Eliminar debiles
        
            strenght_sort = sorted(new_list_result, key = lambda symbol : symbol [2])
            df = pd.DataFrame(strenght_sort, columns= ['Symbol','Tk cross strength','Distance to tk cross'] )
            print(df)
            print("finalizado")

            break

    return df

if trading == None or "No trade":
    trading = test()


    
        # while True:
        #     if get_pos() == None:
        #         if btc_t[1] != 0:
        #             print('BTC is trending')
        #             print("\rAnalizing to trade...", end = '')
        #             from auto_market_order import market_order
        #             print(market_order())
        #         else: #wait
        #             print("BTC is not trending...")
        #     else:
        #         print("There is already a position open: ", get_pos())

        # #crear archivo sym_entry_list
        #mi_path = "K:/Python/Mis programas/Ichibot - copia/market_b.txt"
        # with open(mi_path, "wb") as df:
        #     pickle.dump(sym_entry_list, df)
        # #
        #with open(mi_path, 'r') as df:
        #     sym_entry_list = pickle.load(df)