import math
import numpy as np

def f(x1,x2,x3):
    z=(2*x1+x2+x3)**2+(x1+x2-x3)**2+(x1-x2+3*x3)**2
    return z

def diff(x1,x2,x3):
    f1=12*x1+4*x2+8*x3
    f2=4*x1+6*x2-6*x3
    f3=8*x1-6*x2+22*x3
    return [[f1],[f2],[f3]]

def diff2(x1,x2,x3):
    f11=12
    f12=4
    f13=8
    f22=6
    f23=-6
    f33=22
    return [[f11,f12,f13], [f12,f22,f23],[f13,f23,f33]]

def mat_len(n):
    n=n**2
    a=math.sqrt(np.sum(n))
    return a

x0=np.array([[-1],[1],[-1]])
e=0.00001
b=np.array([[0.0],[0.0],[0.0]])
s=np.array(diff(x0[0][0],x0[1][0],x0[2][0]))
while mat_len(s)>e:
    
    #обратная матрица
    inv=np.linalg.inv(diff2(x0[0][0],x0[1][0],x0[2][0]))

    #произведение матриц
    b[0][0]=s[0][0]*inv[0][0]+s[1][0]*inv[0][1]+s[2][0]*inv[0][2]
    b[1][0]=s[0][0]*inv[1][0]+s[1][0]*inv[1][1]+s[2][0]*inv[1][2]
    b[2][0]=s[0][0]*inv[2][0]+s[1][0]*inv[2][1]+s[2][0]*inv[2][2]

    #новый x0 и J0
    x0=x0-b
    s=np.array(diff(x0[0][0],x0[1][0],x0[2][0]))
print(x0)
print(s)