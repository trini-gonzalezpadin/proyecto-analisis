import numpy as np
import sympy as sp
from sympy import Symbol
from sympy import sympify
from sympy import sin, cos, tan, exp, log, ln, pi
from sympy import integrate

x = sp.Symbol('x')
funcion=input("\nIngrese la funcion en formato explicito ")
funcion = sympify(funcion)#lo pasa a expresion porque era un string
print(funcion)


#pasar Funciones del subespacio a expresion
#s1
funcion11='1'
funcion11=sympify(funcion11)
funcion12='x'
funcion12=sympify(funcion12)
funcion13='x**2'
funcion13=sympify(funcion13)


#s2
#funcion21='cos(pi*x)'
#funcion21=sympify(funcion21)
#funcion22='sen(pi*x)'
#funcion22=sympify(funcion22)

y=funcion*funcion13
print(y)
print(sp.integrate(y,(x,-1,1)))

