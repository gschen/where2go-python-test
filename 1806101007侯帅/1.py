class test:
    def test(self,name):

        return ("hello",name)


if __name__ == '__main__':

    t1=test()
    a=t1.test(input())
    print(a)