import math
sin=math.sin
cos=math.cos
pi=math.pi

def func(x):
    return sin(x)**2
def derrivative(x):
    return 2*cos(x)*sin(x) 
a = - pi/2
b = pi/2
delta = 0.0001
l=(a+b)/2
if derrivative(l)<delta:
    print(l)
else:
    while abs(b-a)> delta:
        if derrivative(l)>0:
            b=l
        else:
             a=l
print(a,b)
    
    
