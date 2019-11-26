def isPrime(q):
    if type(q)==int:
        for i in range(2,q):
            if q%i==0:
                print("False")
                break
        else:
            print("Ture")
    else:
        print("你输入的不是整数")
