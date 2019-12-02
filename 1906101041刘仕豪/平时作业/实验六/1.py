'''
有以下函数，请使用匿名函数进行改造
 def is_even(n):
    return n % 2 == 1
L = list(filter(is_even, range(1, 20)))
'''

L = list(filter(lambda n:n%2==1,range(1, 20)))
print(L)