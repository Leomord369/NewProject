import matplotlib.pyplot as plt
from datetime import datetime, time, date
import pandas as pd
import numpy as np
import persiantools
import sys
import cv2

f = pd.read_csv("BTC-USD.csv")
f["Tolerance"] = f["High"] - f["Low"]
f = f[(f["Date"] >= "2022-06-06") & (f["Date"] < "2023-01-01")]
f["Week"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").isocalendar().week)
wt = f.groupby("Week").sum()
big = np.max(wt["Tolerance"])
bigestweek = wt.loc[wt["Tolerance"] == big]
print(bigestweek)
plt.plot(wt["Tolerance"])
plt.plot([23, 52], [big, big])
print(wt)
plt.show()
