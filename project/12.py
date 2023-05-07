from datetime import datetime
from persiantools.jdatetime import JalaliDate

def miladi_shamsi(str_date):
    str_date = datetime.strptime(str_date.replace("/", "-"),"%Y-%m-%d").date()
    return JalaliDate(str_date)


dates = ["2020-01-01","2021-01-01","2022-01-01"]
print(miladi_shamsi(dates))
