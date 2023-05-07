import numpy as np
import pandas as pd
from datetime import datetime,date,time, timedelta
from persiantools.jdatetime import JalaliDate
import time

# print(pd.date_range("2020-01-01", "2022-01-01",periods=5, freq="H"))
print(pd.date_range("2020-01-01", "2022-01-02",periods=150))




# print(time.time())


# unix time 1970-01-01 00:00:00:000

# print(JalaliDate(1402, 1, 8).to_gregorian())
# print(JalaliDate(1402, 1, 8).toordinal())


# borrow_date = datetime(2023,4,1,12,0,0)
#
# print(borrow_date + timedelta(minutes=152000))



# print(JalaliDate(1402, 1, 8))


# print(JalaliDate.is_leap (1399))
# print(JalaliDate.days_in_month ( 12,1402))

# %Y %m %d %H %M %S

# d = datetime.strptime("2023-08-01", "%Y-%m-%d")
# print(JalaliDate(d))

# print(d.isoweekday())
# print(JalaliDate(d).isoweekday())

# print(datetime.now())
#
# print(date.today())
# print(JalaliDate.today())

# d =date(2023, 4, 28)
# print(JalaliDate(d))
# print(time(16,1,20,800))
#
# print(datetime(2023,4,30,16,1,20,800))

df = pd.read_csv("BTC-USD.csv",index_col="Date")




