from numpy import polynomial
import numpy as np
from scipy import optimize

def f(x):
    return (-1 + x + 0.5*x**3)

root = optimize.newton(f, 0.5)

print(root)