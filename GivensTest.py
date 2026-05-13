from numpy import polynomial
import numpy as np
from scipy import optimize

def givens(row, col, size, using_val, target_val):
    G = np.eye(size)
    r = (using_val**2 + target_val**2)**(1/2)
    G[row][row] = using_val/r
    G[col][col] = using_val/r
    G[col][row] = target_val/r
    G[row][col] = -(target_val/r)
    return G

A = np.array([[6,5,0], [5,1,4], [0,4,3]])
QT = np.eye(3)
for col in range(3):
    for row in range(col + 1, 3):
        G = givens(row, col, 3, A[col][col], A[row][col])
        A = G @ A
        QT = G @ QT


print(A)
print(QT.T)