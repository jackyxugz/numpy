import numpy as np

a = np.arange(9)
print(a)
print("Reduce", np.add.reduce(a))
print("Accumulate", np.add.accumulate(a))
print("Reduceat", np.add.reduceat(a, [0, 5, 2, 7]))
print("Reduceat step I", np.add.reduce(a[0:5]))
print("Reduceat step II", a[5])
print("reduceat step III", np.add.reduce(a[2:7]))
print("reduceat step IV", np.add.reduce(a[7:]))
print("outer")
print(np.add.outer(np.arange(5), a))


