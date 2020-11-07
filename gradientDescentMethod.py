import numpy as np
def func(u):
    x=4*u[0]**2-0.5*u[0]*u[1]+0.5*u[1]**2-9.5*u[0]-3.5*u[1]
    return x
def derrivative(u):
    x1=8*u[0]-0.5*u[1]-9.5
    x2=-0.5*u[0]+u[1]-3.5
    return [x1,x2]
delta= 0.005
u0=np.array([10,10])
J0=np.array(derrivative(u0))
alpha=1
sigma=0.0001
k=0
while np.linalg.norm(J0)>delta:
    k+=1 #количество итераций
    u1=u0-J0*alpha #движение по антиградиенту(минимизация функции)
    if func(u0)>func(u1): #сравнение вывода по функции
        u0=u1 #обновление точки
        J0 = np.array(derrivative(u0))
    else:
        alpha=alpha/2 #дробим альфа
print("uo:",u0,"it number:",k)
print(func(u0))
