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
print('s2: Base trigonométrica:\n\tf1(x)=cos(pix)\n\t' +
          'f2(x)=sen(pix)\n\tf3(x)=1')
print('s3: Polinomios de grado impar hasta 5 :\n\tf1(x)=x' +
          '\n\tf2(x)=x^3\n\tf3(x)=x^5')

print('Elija su opcion ')
op = int(input())


#pasar Funciones del subespacio a expresion
#s1
funcion11='1'
funcion11=sympify(funcion11)
funcion12='x'
funcion12=sympify(funcion12)
funcion13='x**2'
funcion13=sympify(funcion13)

#s2
funcion21='cos(pi*x)'
funcion21=sympify(funcion21)
funcion22='sin(pi*x)'
funcion22=sympify(funcion22)

#s3
funcion31='x'
funcion31=sympify(funcion31)
funcion32='x**3'
funcion32=sympify(funcion32)
funcion33='x**5'
funcion33=sympify(funcion31)

#para la opcion 1: subespacio polinomios grado menor o igual a 2 
#coeficientes de la matriz asociada para sub1 
#cada coefinciente es el producto escalar usual que es la integral de un prodcuto de funciones
if op==1:
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
    mat_A=np.array([[a11,a12,a13],[a12,a22,a23],[a13,a23,a33]])
    print(mat_A)

    #matriz columna de terminos independientes 

    l1=funcion*funcion11
    b1=sp.integrate(l1,(x,c,d))
    l2=funcion*funcion12
    b2=sp.integrate(l2,(x,c,d))
    l3=funcion*funcion13
    b3=sp.integrate(l3,(x,c,d))
    mat_B=np.array([b1,b2,b3])
    print(mat_B)
    # resolver el sistema 
    mat_A_inv = np.linalg.inv(mat_A)
    print('La matriz inversa asociada al sistema es:')
    print(mat_A_inv)
    res= np.matmul(mat_A_inv, mat_B)
    print(res)
    print('La solución del sistema asociado al problemas es: {res}')

else:
    if op==2:

        y11=funcion21*funcion21
        a11=sp.integrate(y11,(x,c,d))

        y12=funcion21*funcion22
        a12=sp.integrate(y12,(x,c,d))


        y22=funcion22*funcion22
        a22=sp.integrate(y22,(x,c,d))

        m1 = np.array([[a11,a12],[a12,a22]])

        #matriz columna de terminos independientes 

        l1=funcion*funcion21
        b1=sp.integrate(l1,(x,c,d))


        l2=funcion*funcion22
        b2=sp.integrate(l2,(x,c,d))

        m2 = np.array([b1,b2])

        # resolver el sistema 
        z=np.linalg.solve(m1,m2)
        print(z)
        print('La solución del sistema asociado al problemas es: {z}')



    else:
        y11=funcion31*funcion31
        a11=sp.integrate(y11,(x,c,d))

        y12=funcion31*funcion32
        a12=sp.integrate(y12,(x,c,d))

        y13=funcion31*funcion33
        a13=sp.integrate(y13,(x,c,d))

        y22=funcion32*funcion32
        a22=sp.integrate(y22,(x,c,d))

        y23=funcion32*funcion33
        a23=sp.integrate(y23,(x,c,d))

        y33=funcion33*funcion33
        a33=sp.integrate(y33,(x,c,d))

        m1 = np.array([[a11,a12,a13],[a12,a22,a23],[a13,a23,a33]])

        #matriz columna de terminos independientes 

        l1=funcion*funcion31
        b1=sp.integrate(l1,(x,c,d))


        l2=funcion*funcion32
        b2=sp.integrate(l2,(x,c,d))

        l3=funcion*funcion33
        b3=sp.integrate(l3,(x,c,d))

        m2 = np.array([b1,b2,b3])

        # resolver el sistema 
        z=np.linalg.solve(m1,m2)
        print(z)
        print('La solución del sistema asociado al problemas es: {z}')







    

    

