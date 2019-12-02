'''
对于整数区间[N，M]，已知0输入说明:两个整数N和M。
输出说明:顺序输出元素数位上各个数字的平方和大于元素本身的数。
输入样例: 21  25
输出样例: 25
说明:
例如22的数位数字为2,2,这两个数字的平方和为8,小于22,不满足筛选条件所以不输出;
25的数位数字为2,5,这两个数字平方和为29,大于25,满足筛选条件，所以将25输出。
'''
N,M = map(int,input().split())
lis = [x for x in range(N,M+1)]
for i in lis:
    if int(str(i)[0])**2 + int(str(i)[1])**2 > i:
        print(i)

