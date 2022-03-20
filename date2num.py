import datetime
import numpy as np


# 星期一 0
# 星期二 1
# 星期三 2
# 星期四 3
# 星期五 4
# 星期六 5
# 星期日 6
def datestr2num(s):
    return datetime.datetime.strptime(s.decode('ascii'), '%Y/%m/%d').date().weekday()


dates, open, high, low, closed = np.loadtxt('data.csv', delimiter=',', usecols=(1, 3, 4, 5, 6),
                                            converters={1: datestr2num}, skiprows=1, unpack=True)

close = closed[:16]
dates = dates[:16]
first_Monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is ", first_Monday)
last_Friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is ", last_Friday)
weeks_indices = np.arange(first_Monday, last_Friday + 2)
print("Weeks indices initial ", weeks_indices)
weeks_indices = np.split(weeks_indices, 3)
print("Weeks indices after split ", weeks_indices)


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]

    return ("APPL", monday_open, week_high, week_low, friday_close)


weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print("Week summary")
print(weeksummary)
np.savetxt('weeksummary.csv', weeksummary, delimiter=',', fmt="%s")
