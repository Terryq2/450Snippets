from numpy import polynomial
import numpy as np
from scipy import optimize
from numpy import linalg as la


A = np.array([1,3])
print(A)
print(A.T)


B = np.array([-1, 4])


print(A.T @ A )

print(A.T @ B)

