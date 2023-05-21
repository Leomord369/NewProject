import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fin = pd.read_csv("BTC-USD.csv")

plt.plot(fin["Date"], fin["Open"], color="yellow", label="Open")
mm = np.min(fin["Open"])
mx = np.max(fin["Open"])
mn = np.mean(fin["Open"])
md = np.median(fin["Open"])
plt.plot([0, 365], [mn, mn], "b--", label="Mean")
plt.plot([0, 365], [md, md], "r--", label="Max")
plt.plot([0, 365], [mx, mx], "g--", label="Median")
plt.plot([0, 365], [mm, mm], "p--", label="Min")
plt.xticks(fin["Date"][::30], rotation=45, color="purple")
plt.yticks(rotation=45, color="pink")
plt.title("FristSaved")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.savefig("Frist.jpg")
plt.show()
