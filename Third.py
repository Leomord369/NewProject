import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import persiantools
import sys
import cv2
from datetime import datetime, time, date, timedelta

money = 1000
f = pd.read_csv("BTC-USD.csv")
f["Benefit"] = f["Close"] - f["Open"]
f["Tolerance"] = f["High"] - f["Low"]
f = f[(f["Date"] >= "2022-06-06") & (f["Date"] < "2022-12-26")]
f["Day"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").day)
f["Weekday"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").isoweekday())
f["Month"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").month)
f["Week"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").isocalendar().week)
ass = len(f) / 7
print(ass)
m = np.array_split(f, ass)
pll = []

for split in m:
    pll.append(money)

    pr = split["Open"]
    pr = list(pr)
    money = money * pr[3]
    pl = split["Close"]
    pl = list(pr)
    money = money / pl[6]

print(money)

plt.plot(pll)
plt.show()
