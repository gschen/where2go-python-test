def xin(z):
    for i in lis[::-1]:
        while z >= i:
            z -= i
            print(i)



lis = [1,2,5,11]
xin(int(input()))
