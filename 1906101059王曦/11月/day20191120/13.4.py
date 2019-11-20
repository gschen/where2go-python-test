#对于给出的长度为N(N< 1000)的正整数数组，满足连续3个元素均为素数的区间称为3素数区间，计算该数组中3素数区间的个数
n = int(input())
s = map(int,input().split())
list1 = list(s)
b = 0
for i in range(n+1):
    z = 0
    if i+3<=n:
        list2 = list1[i:i+3]
        #print(list2)
        for c in list2:
            for a in range(2,c):
                if c%a == 0:
                    break
            else:
                #print(c)
                z = z+1
            if z == 3:
                b += 1
print(b)