def helloWorld():
    print('Hello World')
def hw(helloWorld):
    def x():
        from datetime import datetime
        time = datetime.now()
        print(time)
        helloWorld()
    return x
helloWorld=hw(helloWorld)
helloWorld()
