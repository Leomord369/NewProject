import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import traning
import pandastraning
import sys

Fin = pd.read_csv("BTC-USD.csv")
# y = fin["Close"]-fin["Open"]
# std = np.std(y)
# plt.plot(y)
# plt.plot([0, len(y)], [np.mean(y) - std * 2, np.mean(y) - std * 2], label="down")
# plt.plot([0, len(y)], [np.mean(y) + std * 2, np.mean(y) + std * 2], label="UP")
# plt.plot([0, len(y)], [np.mean(y), np.mean(y)], label="mean")
# plt.legend()
# print(traning.fin["Date"].apply(pandastraning.miladi_Be_shamsi))
# print(fin["Open"].apply(lambda x: int(x)*2))
Fin["Open"] = Fin["Open"].astype(np.uint16)
print(Fin["Open"])
print(type(Fin["Open"]))
print(sys.getsizeof(Fin["Open"]))
