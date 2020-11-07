import math
import numpy as np #использование библиотеки для массивов в питоне
def func(u1,u2,u3):
    return 6*(u1)**2+3*(u2)**2+11*(u3)**2+4*u1*u2-4*u3*u1-6*u2*u3
def derrivative_module(u1,u2,u3):
    A=12*u1+4*u2-4*u3
    B=4*u1+6*u2-6*u3
    C=-4*u1-6*u2+33*u3
    return math.sqrt(A**2+B**2+C**2)
def derrivative(u1,u2,u3):
    n1=12*u1+4*u2-4*u3
    n2=4*u1+6*u2-6*u3
    n3=-4*u1-6*u2+33*u3
    return [[n1],[n2],[n3]]
def derrivative2(u1,u2,u3): #во второй производной появляются константы
    n11=12
    n12=4
    n13=-4
    n22=6
    n23=-6
    n33=33
    return[[n11,n12,n13], [n12,n22,n23],[n13,n23,n33]]
delta=0.0001
u0=np.array([[-1],[1],[-1]])#наше начальное условие
b=np.array([[0.0],[0.0],[0.0]])#чтобы было куда заполнять умножение матриц
ar=np.array(derrivative(u0[0][0],u0[1][0],u0[2][0]))#производная в u0
if derrivative_module(u0[0][0],u0[1][0],u0[2][0])<delta:
    print(u0)
else:
    while derrivative_module(u0[0][0],u0[1][0],u0[2][0])>delta:
        inverse=np.linalg.inv(derrivative2(u0[0][0],u0[1][0],u0[2][0]))#обратная второй производной
        #перемножение матриц поочередно
        b[0][0]=inverse[0][0]*ar[0][0]+inverse[0][1]*ar[1][0]+inverse[0][2]*ar[2][0] #первая строка обратной на первый столбец первой производной и тд
        b[1][0]=inverse[1][0]*ar[0][0]+inverse[1][1]*ar[1][0]+inverse[1][2]*ar[2][0]
        b[2][0]=inverse[2][0]*ar[0][0]+inverse[2][1]*ar[1][0]+inverse[2][2]*ar[2][0]
        u1=u0-b
        u0=u1
print(u0)
