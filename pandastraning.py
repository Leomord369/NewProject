import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, time, date, timedelta
from persiantools.jdatetime import JalaliDate

# fin=pd.read_csv("BTC-USD.csv")
# d=date.today()
# print(JalaliDate(date(2002,11,12)))

# plt.plot((fin["Open"]>30000)|(fin["Close"]>32000))
# plt.show()
miladi_Be_shamsi = lambda x: JalaliDate(datetime.strptime(x, "%Y-%m-%d"))
