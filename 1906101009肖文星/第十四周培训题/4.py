def sum1(n):
    for i in lis:
        while n >= i:
            n -= i
            print(i)
lis = [11,5,2,1]
sum1(int(input()))