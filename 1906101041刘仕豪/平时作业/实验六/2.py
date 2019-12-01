'''
有helloWorld()函数，请使用装饰器，在每次调用该函数的时候可以显示当前时间，注意引入datatime
def helloWord（）：
    print（‘Hello wolrd’）
'''
import datetime
def func(function):
    t = datetime.datetime.now()
    print(t)
    return function
@func
def helloWord():
    print('Hello wolrd')
helloWord()