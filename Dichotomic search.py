import math

sin = math.sin
pi=math.pi

def function(x):
    return sin(x)**2
a = -pi/2 
b = pi/2

delta = 0.01
e = 0.001

while abs(b - a) > delta:
    lambda1 = (a + b) / 2 - e
    lambda2 = (a + b) / 2 + e

    func_at_lambda_2 = function(lambda2)
    func_at_lambda_1 = function(lambda1)

    if func_at_lambda_2 > func_at_lambda_1:
        b = lambda2
    else:
        a = lambda1

print(a, b)
