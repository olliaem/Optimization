import numpy as np
def func(u):
    x=4*u[0]**2-0.5*u[0]*u[1]+0.5*u[1]**2-9.5*u[0]-3.5*u[1]
    return x
def derrivative(u):
    x1=8*u[0]-0.5*u[1]-9.5
    x2=-0.5*u[0]+u[1]-3.5
    return [x1,x2]
def projection (u):
    if u[0]<-5:
        u[0]=-5
    if u[1]<-2:
        u[1]=-2
    if u[0]>3:
        u[0]=3
    if u[1]>6:
        u[1]=6
    return u
delta= 0.005
u0=np.array([100,1000])
J0 = np.array(derrivative(u0))
alpha=1
sigma=0.0001
k=0
while np.linalg.norm(J0)>delta:
    k+=1 #количество итераций
    u1=u0-J0*alpha #движение по антиградиенту
    u1=projection(u1) #проекцирование точки 
    if func(u0)>func(u1): #сравнение вывода по функции
        u0=u1 #обновление точки
    else:
        alpha=alpha/2 #дробим альфа
    J0 = np.array(derrivative(u0))
    if alpha<sigma: #чтобы прекратить бесконечное дробление альфа
        break
print("uo:",u0,"iteration:",k)
print(func(u0))
   
    
    
    
    
    
