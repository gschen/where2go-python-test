def isPrime(x):
    if type(x)==int:
        for i in range(2,x):
            if x % i==0:
                print("false")
                break
            else:print("true")
    else:print("你输入的数字不为整数")
                    
