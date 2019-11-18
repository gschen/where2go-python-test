#输出数组中的偶数
N = int(input())
list = list(map(int,input().split()))
for i in list:
    if i%2 == 0:
        print('{:>1}'.format(i),end=' ')
