from numpy import polynomial
import numpy as np
from scipy import optimize
from numpy import linalg as la

def f(x):
    return (-1 + x + 0.5*x**3)

root = optimize.newton(f, 0.5)

print(root)

def g(x, y):
    first_component = x+2*y - 2
    second_component = x**2 +4*y**2 - 4 
    return np.array([first_component, second_component])

def jacobian(x, y):
    return np.array([[1, 2], [2*x, 8*y]])

def newton(step_num):
    x = np.array([1, 2])
    for k in range (step_num):
        s = la.solve(jacobian(x[0], x[1]), -1 * g(x[0], x[1]))
        x = x+ s
        print("Iteration", k, x)
    return x

newton(100)