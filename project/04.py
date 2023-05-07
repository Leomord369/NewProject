import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv",index_col="Date")

print(df[["Open","Close"]])