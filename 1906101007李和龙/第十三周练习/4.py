"""
17.对于整数区间[N，M]，已知0输入说明:两个整数N和M。
输出说明:顺序输出元素数位上各个数字的平方和大于元素本身的数。
输入样例: 21  25
输出样例: 25
说明:例如22的数位数字为2,2,这两个数字的平方和为8,小于22,不满足筛选条件所以不输出; 25的数位数字为2,5,这两个数字平方和为29,大于25,满足筛选条件，所以将25输出。


"""
m,n=map(int,input().split())
for i in range(m,n+1):
    s = 0
    for m in str(i):
        s = s + int(m)**2
    if s > i:
        print(i)

