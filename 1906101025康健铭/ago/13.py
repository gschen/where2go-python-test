def fib(x):
    n=0,a=1,b=2
    while n<x:
        yield a
        a=b,b=a*b
        
        
