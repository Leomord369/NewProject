import numpy as np
import pandas as pd

df = pd.read_csv("BTC-USD.csv")

# print(df.shape)
# print(df.values.reshape((7, 366)))

data = df.iloc[1:101]

splits = np.split(data,10)

for split in splits:
    print(split.describe())
    input()