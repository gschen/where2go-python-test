#时间装饰器
import functools
import datetime
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(datetime.datetime.now())
        return func(*args, **kw)
    return wrapper
@log
def helloword():
    print('Hello world')
helloword()