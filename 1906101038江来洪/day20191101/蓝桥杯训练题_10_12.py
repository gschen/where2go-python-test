#ABCDE * ? = EDCBA求出这个数字
def daoxu(x):
    list = []
    for i in x:
        list.append(i)
    list.reverse()
    return int(''.join(list))
z = 10000
s = 0
while z<= 99999:
    for y in range(2,10):
        x = str(z)
        if z*y == daoxu(x):
            print(z)
    z += 1
