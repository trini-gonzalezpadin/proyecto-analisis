import numpy as np
import sympy as sp
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')

a=np.array([[2,4,6],[4,5,6],[3,1,-2]])
b=np.array([18,24,4])
x=np.linalg.solve(a,b)
print(x)

