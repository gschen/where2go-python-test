'''
def foo():
    print('王卓越憨批')
def f():
    print('王卓越憨批')
    f()
def g(n):
    print(n)

    if n == 10:
        return None
    g(n + 1)
g(1)
'''
import PyInstaller
#前100求和
'''
def sum100(n):
    if n== 101 :
        return
    return n+(n+1)
print(sum100(10))
'''
class text:
    def __init__(self):
        self.a=123
class test01:
    a = 123
    b = 456
    def aadd(self,a,b):
        return (a+b)
n = test01()

class ttt:
    def __init__(self,a,b):
        self.a = a

