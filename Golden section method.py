import math
sin=math.sin
pi=math.pi

def F(x):
    return sin(x)**2

g = 0.618
a = -pi/2
b = pi/2
l = a + (b - a) * (1 - g)
m = a + (b - a) * g 
Fm = F(m)
Fl = F(l)
delta = 0.001
    
while abs(b - a) > delta:
    if Fl < Fm:
        b = m
        m = l
        Fm = Fl
        l = a + (1 - g) * (b - a)
        Fl=F(l)
    else:
        a = l
        l = m
        Fl = Fm
        m = a + g * (b - a)
        Fm=F(m)
            
print(a, b)

