import numpy as np
import pandas as pd
from datetime import datetime
from persiantools.jdatetime import JalaliDate

df = pd.read_csv("BTC-USD.csv")

# print(df["Open"].apply(lambda x: x * 3))
# print(df["Open"].apply(lambda price: int(price)))

# def miladi_shamsi(str_date):
#     str_date = datetime.strptime(str_date.replace("/", "-"),"%Y-%m-%d").date()
#     return JalaliDate(str_date)
#
#
# print(df["Date"].apply(miladi_shamsi))
# print(df["Date"].apply(miladi_shamsi))
#
# print(df["Date"].apply(lambda str_date:JalaliDate(datetime.strptime(str_date.replace("/", "-"),"%Y-%m-%d").date())))

