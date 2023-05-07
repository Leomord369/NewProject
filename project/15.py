import numpy as np
import pandas as pd
from datetime import datetime
from persiantools.jdatetime import JalaliDate

df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]

# df["Open"] = df["Open"].astype("int")
df["Open"] = df["Open"].astype(np.uint32)
df["High"] = df["High"].round(2)
df["Benefit"] = df["Benefit"].abs()
print(df)

# x = np.arange(1,100)
#
# x = x.astype(np.float64)
#
# print(x)
# print(x.dtype)
