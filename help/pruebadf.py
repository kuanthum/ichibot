import pandas as pd

symbol = ['btcusdt', 'etcusdt', 'axsusdt']
position_value = [0, 0, 1]

d = {'symbol': symbol, 'position_value': position_value}

df = pd.DataFrame(d)


index = 0
for i in df['position_value']:
    index += 1
    if i != 0:
        print(df.loc[index-1])

