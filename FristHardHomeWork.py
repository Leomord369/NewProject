from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = pd.read_csv("BTC-USD.csv")
f = f[(f["Date"] >= "2022-06-01") & (f["Date"] < "2023-01-01")]
f["Benefit"] = f["Close"] - f["Open"]
f["Day"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").day)
f["Weekday"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").isoweekday())
f["Month"] = f["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").month)

Gpmonth = f.groupby("Month").sum()
MaxM = np.max(Gpmonth["Benefit"])
MinM = np.min(Gpmonth["Benefit"])
print("Max Benefit is for month:", Gpmonth.loc[Gpmonth["Benefit"] == MaxM])
print("Min Benefit is for month:", Gpmonth.loc[Gpmonth["Benefit"] == MinM])
plt.plot(Gpmonth["Benefit"])
plt.plot([6, 12], [MaxM, MaxM], label="Max")
plt.plot([6, 12], [MinM, MinM], label="Min")
plt.xlabel("Month")
plt.ylabel("Benefit")
plt.legend()
plt.show()
