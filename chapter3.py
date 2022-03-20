import numpy as np

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), skiprows=1, unpack=True)
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), skiprows=1, unpack=True)
t = np.arange(len(c))
print("VWAP = ", np.average(c, weights=v))
print("mean =", np.mean(c))
print("twap =", np.average(c, weights=t))
print("highest = ", np.max(h))
print("loweset = ", np.min(l))
print("Spread high price", np.ptp(h))
print("Spread low price", np.ptp(l))
