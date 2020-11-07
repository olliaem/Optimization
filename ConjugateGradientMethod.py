import numpy as np
def func(u):
    x=4*u[0]**2+2*u[0]*u[1]+2*u[1]*u[2]+3*u[1]**2+2*u[2]**2-u[0]+u[1]-u[2]-1
    return x
def derrivative(u):
    x1=8*u[0]-2*u[1]-1
    x2=2*u[0]+2*u[2]+6*u[1]+1
    x3=2*u[1]+4*u[2]-1
    return [x1,x2,x3]
def find_alpha(func,a,b):
    l=a+(b-a)*0.382
    m=a+(b-a)*0.618
    while abs(b-a)>0.005:
        if func(l)<func(m):
            b=m
            m=l
            l=a+(0.382)*(b-a)
        else:
            a=l
            l=m
            m=a+0.618*(b-a)
    return (a+b)/2
def f(alpha):
    return func(u0-J0*alpha)
delta=0.005
u0=np.array([10,0,-1])
J0=np.array(derrivative(u0))
while np.linalg.norm(J0)>delta:
    alpha=find_alpha(f,0,1)
    u1=u0-alpha*J0
    J1=np.array(derrivative(u1))
    if np.linalg.norm(J1)<delta:
        u0=u1
    else:
        t=(np.linalg.norm(J0))**2
        k=(np.linalg.norm(J1))**2
        betta=(k/t)
        J1=J1-betta*J0
        u0=u1
        J0=J1
print("u0:",u0)
print(func(u0))
