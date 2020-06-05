import numpy as np
import sympy as sp
from sympy import Symbol
from sympy import sympify
from sympy import sin, cos, tan, exp, log, ln, pi
from sympy import integrate
from numpy import array
x = sp.Symbol('x')
funcion=input("\nIngrese la funcion en formato explicito ")
funcion = sympify(funcion)#lo pasa a expresion porque era un string
print(funcion)

print('Escriba el intervalo de aproximacion de la funcion:')
c = float(input())
d = float(input())
print('Subespacios disponibles:')

print('s1: Polinomios de grado menor o igual a dos:\n\tf1(x)=1' +
          '\n\tf2(x)=x\n\tf3(x)=x^2')



#pasar Funciones del subespacio a expresion
#s1
funcion11='1'
funcion11=sympify(funcion11)
funcion12='x'
funcion12=sympify(funcion12)
funcion13='x**2'
funcion13=sympify(funcion13)




#para la opcion 1: subespacio polinomios grado menor o igual a 2 
#coeficientes de la matriz asociada para sub1 
#cada coefinciente es el producto escalar usual que es la integral de un prodcuto de funciones
y11=funcion11*funcion11
a11=sp.integrate(y11,(x,c,d))
y12=funcion11*funcion12
a12=sp.integrate(y12,(x,c,d))

y13=funcion11*funcion13
a13=sp.integrate(y13,(x,c,d))

y22=funcion12*funcion12
a22=sp.integrate(y22,(x,c,d))

y23=funcion12*funcion13
a23=sp.integrate(y23,(x,c,d))

y33=funcion13*funcion13
a33=sp.integrate(y33,(x,c,d))

    #matriz de coeficientes del sistema 
matA=np.array([[a11,a12,a13],[a12,a22,a23],[a13,a23,a33]])
print(matA)
matA_inv=np.linalg.inv(matA)
print(matA_inv)



    #matriz columna de terminos independientes 
print('para B')
l1=funcion*funcion11
b1=sp.integrate(l1,(x,c,d))


l2=funcion*funcion12
b2=sp.integrate(l2,(x,c,d))

l3=funcion*funcion13
b3=sp.integrate(l3,(x,c,d))

m2=np.array([b1,b2,b3])
print(m2)

# resolver el sistema 

res=np.matmul(matA_inv, m2)
print(res)


#z=np.linalg.solve(m1,m2)
#print(z)
#print('La solución del sistema asociado al problemas es: {z}')