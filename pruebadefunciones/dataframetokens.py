import pandas as pd
from metkc_periods import new_list
#s,tk_strengt, tk_distance

# list = [
# ['EOSUSDT', 4, 'strong', 19], 

strenght_sort = sorted(new_list, key = lambda symbol : symbol [3])
print(strenght_sort)


df = pd.DataFrame(strenght_sort, columns= ['Symbol','Price','Ichi Score', 'Distance to tk cross', 'Tk cross strength'] )

print(df)