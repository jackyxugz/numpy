import numpy as np

a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
print("Divide", np.divide(a, b), np.divide(b, a))
print("True_divide", np.true_divide(a, b), np.true_divide(b, a))
print("Floor_divide", np.floor_divide(a, b), np.floor_divide(b, a))
print(a, b)
c = 3.14 * b
print(a / b, b / a)
print(c // b, b // c)
print(a // b, b // a)
