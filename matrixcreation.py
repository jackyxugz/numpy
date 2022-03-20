import numpy as np

A = np.mat("1 2 3;4 5 6;7 8 9")
B = np.eye(3)
C = 2 * B

print("Create from string:", A)
print(B)
print(C)
print("transpose A", A.T)
print("Creation from array", np.mat(np.arange(9).reshape(3, 3)))
print("Compound matrix\n", np.bmat("B C;C B"))
