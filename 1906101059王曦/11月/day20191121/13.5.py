# 对于整数区间[N，M]，已知0输入说明:两个整数N和M。
# 输出说明:顺序输出元素数位上各个数字的平方和大于元素本身的数
n = int(input())
m = int(input())
for i in range(n,m+1):
    list1 = list(str(i))
    #print(list1)
    s = 0
    for a in list1:
        s = int(a)**2+s
    #print(s)
    if s>i:
        print(i)