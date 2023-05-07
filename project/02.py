import pandas as pd

df = pd.read_csv("data.csv",index_col="id")

print(df.iloc[0:2])
print(df.loc[1000:1002])

