'''
动态规划求解斐波那契数列问题

1,1,2,3,5,8,13,...

top-down 方式求解
'''

def f(n):
    a = [0] * (n+1)
    a[0] = 1
    a[1] = 1
    
    return g(n, a)

def g(n, a):

    if a[n] > 0:
        return a[n]
    
    a[n] = g(n-1,a) + g(n-2, a)

    return a[n]

print(f(5))
