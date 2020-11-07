import math
sin=math.sin
pi=math.pi

def func(x):
    return sin(x)**2

def num_fib(N):
    t=[1, 1]
    i = 1
    while t[i]<=N:
        t.append(t[i] + t[i - 1])
        i=i+ 1
    return t
def main():
    a=-pi/2
    b=pi/2
    delta=0.1
    fib=num_fib((b-a)/delta)
    j=len(fib)-1
    d=(b-a)/fib[j]
    l=a+fib[j-2]*d  
    m=a+fib[j-1]*d
    j=j-1
    print(fib)
    while j>=2:
        if func(l)<func(m):
            b==m
            m==l
            func(m)==func(l)
            d==(b-a)/fib[j]
            l==a+fib[j-2]*d
        else:
            a==l
            l==m
            func(l)==func(m)
            d==(b-a)/fib[j]
            m==a+fib[j-1]*d
        j=j-1
    print(l, m)

if __name__=='__main__':
    main()
    
    

    



        
