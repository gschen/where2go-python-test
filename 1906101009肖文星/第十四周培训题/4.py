lis = [11,5,2,1]
def sum1(n):
    for i in lis:
        while n >= i:
            n -= i
            print(i)
sum1(int(input()))