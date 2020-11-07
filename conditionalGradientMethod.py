import numpy as np
def func(u):
    x=u[0]**2+u[0]*u[1]+u[1]**2
    return x
def derrivative(u):
    x1=2*u[0]+u[1]
    x2=u[0]+2*u[1]
    return [x1,x2]
def findingU_bar(u_bar):
    if derrivative(u0)[0]>0:
        u_bar1=0
    if derrivative(u0)[0]<0:
        u_bar1=3
    if derrivative(u0)[1]>0:
        u_bar2=0
    if derrivative(u0)[1]<0:
        u_bar2=4
    return u_bar
delta= 0.005
u0=np.array([1,-1])
J0 = np.array(derrivative(u0))
alpha=1
sigma=0.0001
while np.linalg.norm(J0)>delta:
    t=findingU_bar(u0)
    u1=u0+alpha*(t-u0)
    J1=np.array(derrivative(u1))
    if func(u0)>func(u1):
        u0=u1
        J0=J1
    else:
        alpha=alpha/2
    if alpha<sigma:
         break
print("uo:",u0)
print(func(u0))
