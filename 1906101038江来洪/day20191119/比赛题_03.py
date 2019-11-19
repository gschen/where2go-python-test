#输出数组中的6的倍数
N = int(input())
list = list(map(int,input().split()))
for i in list:
    if i%6 == 0:
        print('{:>1}'.format(i),end=' ')
