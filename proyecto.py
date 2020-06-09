import numpy as np
import sympy as sp
from sympy import Symbol
from sympy import sympify
from sympy import sin, cos, tan, exp, log, ln, pi
from sympy import integrate
funcion=''
x = sp.Symbol('x')
while (funcion==''):
    try:
        funcion=input('\nIngrese la funcion en formato explicito como se muestra:\n\tPolinómicas: ax**2+b*x+c'+
        '\n\tTrigonométricas: sin(x) ,cos(x)'+'\n\tExponenicales :exp(x)\n\t')
        funcion=sympify(funcion)
    except Exception:
        funcion=''
        print("Ingreso incorrecto de la funcion.Porfavor vuelva a intentarlo")
#funcion=input("\nIngrese la funcion en formato explicito ")
#funcion = sympify(funcion)#lo pasa a expresion porque era un string
print(funcion)

print('Escriba el intervalo de aproximacion de la funcion:')
c = float(input())
d = float(input())
print('Subespacios disponibles:')
print('s1: Polinomios de grado menor o igual a dos:\n\tf1(x)=1' +
          '\n\tf2(x)=x\n\tf3(x)=x²')
print('s2: Base trigonométrica:\n\tf1(x)=cos(pix)\n\t' +
          'f2(x)=sen(pix)\n\tf3(x)=1')
print('s3: Polinomios de grado impar hasta 5 :\n\tf1(x)=x' +
          '\n\tf2(x)=x³\n\tf3(x)=x⁵')
print('s4: Recta:\n\tf1(x)=1\n\t' +
          'f2(x)=x')

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
funcion33=sympify(funcion33)

#s4
funcion41='1'
funcion41=sympify(funcion41)
funcion42='x'
funcion42=sympify(funcion42)


#para la opcion 1: subespacio polinomios grado menor o igual a 2 
#coeficientes de la matriz asociada para sub1 
#cada coefinciente es el producto escalar usual que es la integral de un prodcuto de funciones
if op==1:
    # Genero las matrices, una columna y otra cuadrada de 3x3, vacias:
    matrizB = np.zeros(3)
    matrizA = np.zeros((3, 3))
    
    y11=funcion11*funcion11
    y12=funcion11*funcion12
    y13=funcion11*funcion13
    y22=funcion12*funcion12
    y23=funcion12*funcion13
    y33=funcion13*funcion13
    
    # Calculo de Matriz A:

    matrizA[0][0] = sp.integrate(y11,(x,c,d))
    matrizA[0][1] = sp.integrate(y12,(x,c,d))
    matrizA[0][2] = sp.integrate(y13,(x,c,d))

    matrizA[1][0] = sp.integrate(y12,(x,c,d))
    matrizA[1][1] = sp.integrate(y22,(x,c,d))
    matrizA[1][2] = sp.integrate(y23,(x,c,d))

    matrizA[2][0] = sp.integrate(y13,(x,c,d))
    matrizA[2][1] =sp.integrate(y23,(x,c,d))
    matrizA[2][2] = sp.integrate(y33,(x,c,d))
            
    print('Matriz A = ',matrizA)
    #matriz columna B
    l1=funcion*funcion11
    l2=funcion*funcion12
    l3=funcion*funcion13
    
    matrizB[0] = sp.integrate(l1,(x,c,d))
    matrizB[1] = sp.integrate(l2,(x,c,d))
    matrizB[2] = sp.integrate(l3,(x,c,d))

    print('Matriz B = ',matrizB)
    
    # Resuelvo el sistema de ecuaciones
    matrizAInv = np.linalg.inv(matrizA)
    matrizX = np.matmul(matrizAInv,matrizB)

    print('Coeficientes = ',matrizX)
    print('La mejor aproximacion de la funcion es : {} + {} x + {} x²'.format(matrizX[0], matrizX[1], matrizX[2]))
    #print ('La mejor aproximacion de la funcion es :', matrizX[0],'.1+',matrizX[1],'.x+',matrizX[2],'.x^2')

else:
    if op==2:
        # Genero las matrices, una columna y otra cuadrada , vacias:
        matrizB = np.zeros(2)
        matrizA = np.zeros((2, 2))
       
        y11=funcion21*funcion21
        y12=funcion21*funcion22
        y22=funcion22*funcion22
        
        matrizA[0][0] = sp.integrate(y11,(x,c,d))
        matrizA[0][1] = sp.integrate(y12,(x,c,d))
        matrizA[1][0] = sp.integrate(y12,(x,c,d))
        matrizA[1][1] = sp.integrate(y22,(x,c,d))
        print('Matriz A = ',matrizA)
      
        #matriz columna B 
        l1=funcion*funcion41
        l2=funcion*funcion42
        matrizB[0] = sp.integrate(l1,(x,c,d))
        matrizB[1] = sp.integrate(l2,(x,c,d))
        print('Matriz B = ',matrizB)

        # Resuelvo el sistema de ecuaciones
        matrizAInv = np.linalg.inv(matrizA)
        matrizX = np.matmul(matrizAInv,matrizB)

        print('Coeficientes = ',matrizX)
        print('La mejor aproximacion de la funcion es : {} cos(pix)+ {}sen(pix)'.format(matrizX[0], matrizX[1]))

    else:
        if op==3:
            # Genero las matrices, una columna y otra cuadrada de 3x3, vacias:
            matrizB = np.zeros(3)
            matrizA = np.zeros((3, 3))
            y11=funcion31*funcion31
            y12=funcion31*funcion32
            y13=funcion31*funcion33
            y22=funcion32*funcion32
            y23=funcion32*funcion33
            y33=funcion33*funcion33
        
            
            # Calculo de Matriz A:
            # para definir las funciones que van en la intregal
            # las calcule cada una.

            matrizA[0][0] = sp.integrate(y11,(x,c,d))
            matrizA[0][1] = sp.integrate(y12,(x,c,d))
            matrizA[0][2] = sp.integrate(y13,(x,c,d))

            matrizA[1][0] = sp.integrate(y12,(x,c,d))
            matrizA[1][1] = sp.integrate(y22,(x,c,d))
            matrizA[1][2] = sp.integrate(y23,(x,c,d))

            matrizA[2][0] = sp.integrate(y13,(x,c,d))
            matrizA[2][1] =sp.integrate(y23,(x,c,d))
            matrizA[2][2] = sp.integrate(y33,(x,c,d))
                    
            print('Matriz A = ',matrizA)
            #matriz columna B
            l1=funcion*funcion31
            l2=funcion*funcion32
            l3=funcion*funcion33
            
            matrizB[0] = sp.integrate(l1,(x,c,d))
            matrizB[1] = sp.integrate(l2,(x,c,d))
            matrizB[2] = sp.integrate(l3,(x,c,d))

            print('Matriz B = ',matrizB)
            
            # Resuelvo el sistema de ecuaciones
            matrizAInv = np.linalg.inv(matrizA)
            matrizX = np.matmul(matrizAInv,matrizB)

            print('Coeficientes = ',matrizX)
            print('La mejor aproximacion de la funcion es : {}x + {}x³ + {}x⁵'.format(matrizX[0], matrizX[1], matrizX[2]))

        else:
            # Genero las matrices, una columna y otra cuadrada , vacias:
            matrizB = np.zeros(2)
            matrizA = np.zeros((2, 2))


            y11=funcion41*funcion41
            y12=funcion41*funcion42
            y22=funcion42*funcion42

            matrizA[0][0] = sp.integrate(y11,(x,c,d))
            matrizA[0][1] = sp.integrate(y12,(x,c,d))
            matrizA[1][0] = sp.integrate(y12,(x,c,d))
            matrizA[1][1] = sp.integrate(y22,(x,c,d))
            print('Matriz A = ',matrizA)


            #matriz columna B 
            l1=funcion*funcion41
            l2=funcion*funcion42

            matrizB[0] = sp.integrate(l1,(x,c,d))
            matrizB[1] = sp.integrate(l2,(x,c,d))
            print('Matriz B = ',matrizB)

            # Resuelvo el sistema de ecuaciones
            matrizAInv = np.linalg.inv(matrizA)
            matrizX = np.matmul(matrizAInv,matrizB)

            print('Coeficientes = ',matrizX)
            print('La mejor aproximacion de la funcion es : {} + {} x '.format(matrizX[0], matrizX[1]))


            
        




        







    

    

