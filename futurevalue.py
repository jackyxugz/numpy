import matplotlib.pyplot as plt
import numpy_financial as npf

print("Future value", npf.fv(0.03 / 4, 5 * 4, -10, -1000))
fvals = []

for i in range(1, 12):
    fvals.append(npf.fv(0.0195 / 12, i * 4, -10, -1000000))

print(fvals)
plt.plot(range(1, 12), fvals, 'bo')
plt.title("Future value, 3 % interest, \n Quarterly payment of 10")
plt.ylabel("Future value")
plt.grid()
plt.legend(loc='best')
plt.show()
