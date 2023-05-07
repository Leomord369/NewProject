import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv")

print(df[(df["Close"]>40000) | (df["Open"]> 30000)])
# print(df["Date"][df["Open"]> 30000])