import math
Pi=math.pi
sin=math.sin
a=-Pi/2
b=Pi/2
N=1000
h=(b-a)/N
e=h/100
def func(u):
    return sin(u)**2
u=a
min_value=func(u)
min_parameter=u
for i in range(N):
    u=a+(i+1)*h
    current_value=func(u)
    if current_value < min_value:
        min_value = current_value
        min_parameter = u
        
left_par = min_parameter - e
left_value = func(left_par)

right_par = min_parameter + e
right_value = func(right_par)

if left_value < min_value:
    min_value = left_value
    min_parameter = left_par

if right_value < min_value:
    min_value = right_value
    min_parameter = right_par
    
print(min_parameter, min_value)
