import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv")
df["benefit"]=df["Open"]-df["Close"]
data = df.iloc[1:361]
splits = np.split(data,30)


