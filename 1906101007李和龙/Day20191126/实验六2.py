"""
2. 有helloWorld()函数，请使用装饰器，在每次调用该函数的时候可以显示当前时间，注意引入datatime
def helloWord（）：
print（‘Hello wolrd’）

"""

from datetime import datetime
def now(func):
    def wrapper(*args,**kw):
        print(datetime.now())
        return func(*args,**kw)
    return wrapper
@now
def helloWord():
    return 'Hello world'

print(helloWord())
