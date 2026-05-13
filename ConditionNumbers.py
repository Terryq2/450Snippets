from numpy import polynomial
import numpy as np
from scipy import optimize
from numpy import linalg as la


A = np.array([[3, 1], [0, 0.5]])
c_1 = np.array([3, 4])



print(la.cond(A, 1))
print(la.cond(A, 2))
print(la.cond(A, np.inf))


print(102/12 * (10**(-11)/1.3))

print(la.norm(c_1))

print(2/(2)**(1/2))
