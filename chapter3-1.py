import numpy as np

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True, skiprows=1)
print("median =", np.median(c))
sorted1 = np.msort(c)
#print("sorted =", sorted1)
N = len(sorted1)
#print(N)
print("average middle =", (sorted1[int(N / 2)] + sorted1[(int((N - 1) / 2))]) / 2)
print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean()) ** 2))
