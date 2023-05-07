import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv",index_col="Date")



# df["Jadid"] = 0

df["Benefit"] = df["Close"] - df["Open"]
df["Tolerance"] = df["High"] - df["Low"]

print(df[["Open","Close","Benefit","Tolerance"]])