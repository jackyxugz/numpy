import numpy as np
import datetime


def date2num(s):
    return datetime.datetime.strptime(s.decode('ascii'), '%Y/%m/%d').date().weekday()


dates, closes = np.loadtxt('data.csv', delimiter=',', usecols=(1, 6), converters={1:date2num}, skiprows=1, unpack=True)
indices = np.lexsort((dates, closes))

print("Indices", indices)
print(["%s %s" % (datetime.date.fromordinal(int(dates[i])), closes[i]) for i in indices])