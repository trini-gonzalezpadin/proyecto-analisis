
import sympy
sympy.init_printing()
x,y = sympy.symbols('x,y')

Poly1 = sympy.Poly(1)
Poly2 = sympy.Poly(x)
Poly3=sympy.Poly(x*2)

def mult(p1, p2):
    return p1 * p2



print(mult(Poly1,Poly2))