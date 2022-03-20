import sys
from datetime import datetime
import numpy as np


def NumpySum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


def PythonSum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i] + b[i])
    return c


size = int(sys.argv[1])
start = datetime.now()
c = PythonSum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("Pythonsum elapsed time in microseconds", delta.microseconds)
start = datetime.now()
c = NumpySum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPysum elapsed time in microseconds", delta.microseconds)
