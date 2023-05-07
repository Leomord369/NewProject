import numpy as np
import pandas as pd
from datetime import datetime
from persiantools.jdatetime import  JalaliDate

df = pd.read_csv("BTC-USD.csv")
df = df[(df["Date"]>= "2022-06-01") & (df["Date"]<"2023-01-01")]

df["Month"] = df["Date"].apply(lambda d : datetime.strptime(d, "%Y-%m-%d").month)
df["Day"] = df["Date"].apply(lambda d : datetime.strptime(d, "%Y-%m-%d").day)
df["WeekDay"] = df["Date"].apply(lambda d : datetime.strptime(d, "%Y-%m-%d").isoweekday())
df["Benefit"] = df["Close"] - df["Open"]
df["Status"] = df["Benefit"].apply(lambda x: 1 if x>0 else -1)

# df["Jalali"] = df["Date"].apply(lambda d : JalaliDate(datetime.strptime(d, "%Y-%m-%d")))
# df["Month"] = df["Date"].apply(lambda d : JalaliDate(datetime.strptime(d, "%Y-%m-%d")).month)
# df["Day"] = df["Date"].apply(lambda d : JalaliDate(datetime.strptime(d, "%Y-%m-%d")).day)
# df["WeekDay"] = df["Date"].apply(lambda d : JalaliDate(datetime.strptime(d, "%Y-%m-%d")).isoweekday())


# print(df.groupby("Month").sum())

print(df[df["WeekDay"] == 1])

