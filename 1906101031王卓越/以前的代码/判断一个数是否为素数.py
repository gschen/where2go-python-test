def isPrime(n):
    i=0
    for k in range(2,n-1):
        if n%k==0:
            i=1
            print("False")
            break
    if i==0:
        print("True")    
    return
isPrime(n=int(input("请输入参数：")))
#王卓越