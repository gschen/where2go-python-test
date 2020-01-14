from datetime import *
def log(func):
    def wrapper(*args,**kw):
        print('call % s():'%func._name_)
        return func(*args,**kw)
    return wrapper
@log
def haha():
    print(datetime.now())
haha()