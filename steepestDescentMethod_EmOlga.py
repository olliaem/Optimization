import numpy as np
def func(u):
        x=4*u[0]**2-0.5*u[0]*u[1]+0.5*u[1]**2-2.2*u[0]-1.8*u[1]
        return x
def derrivative(u):
        x1=8*u[0]-0.5*u[1]-2.2
        x2=-0.5*u[0]+u[1]-1.8
        return [x1,x2]
def f(alpha):
        return func(u0 - alpha*J0)
def find_alpha(func,a,b):
        l=a+(b-a)*(0.382)
        m=a+(b-a)*0.618
        while abs(b-a)>0.001:
                if func(l)<func(m):
                        b=m
                        m=l
                        l=a+(0.382)*(b-a)
                else:
                        a=l
                        l=m
                        m=a+0.618*(b-a)
        d=(a+b)/2
        return d
u0 = np.array([12,50])    
J0 = np.array(derrivative(u0))
print(J0)
delta = 0.001
while np.linalg.norm(J0)>delta:
    J0 = np.array(derrivative(u0))
    alpha = find_alpha(f,0,1)
    u0=u0-J0*alpha
print(alpha)
print("u0: ",u0)
print(func(u0))
