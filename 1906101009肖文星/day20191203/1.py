'''递归：函数不断调用其自身'''
'''def a(n):
    print(n)#无条件限制
    a(n+1)
a(1)'''
def a(n):
    if n==10:
        return
    print(n)#有条件限制
    a(n+1)
a(1)