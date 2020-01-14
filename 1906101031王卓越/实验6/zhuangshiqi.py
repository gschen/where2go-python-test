from datetime import*
def raw(jkl):
    def ad(*args,**kw):
        print("当前时间：",datetime.now())
        return jkl(*args,**kw)
    return ad
@raw # hellooworld=raw(hellworld)
def helloworld():
    print('hello,world')
helloworld()
#王卓越
