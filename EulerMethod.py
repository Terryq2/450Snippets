from numpy import polynomial
import numpy as np 
from numpy import array
from scipy import optimize
from numpy import linalg as la


A = array([[-3, 1],[1, -3]])
y0 = array([1, 0])

y1 = y0 + 0.25* (A@y0)

print(y1)




y1_backward_euler = la.solve(np.eye(2)-0.25*A, y0)



print(np.eye(2)-0.25*A)
# print(y1_backward_euler)