import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv",index_col="Date")

df.columns = ['a','b','c','d','e','f']
df.index=[np.arange(100,466,1)]


print(df)
