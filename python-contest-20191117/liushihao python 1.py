'''
16.将整数数组中是6的倍数的元素按照输入次序依次输出。如果没有符合条件的元素则输出-1。
输入说明:第一-行是整数N (N<10000) ，表示数组中的元素个数,第二行是这个数组中的N个元素,规
定元素中至少包含-个满足条件的元素。
输出说明:输出数组序列中6的倍数,如果有两个以上满足条件的元素，中间用空格隔开。
输入样例: 6
2 3 6 12 28 45
输出样例: 6 12
'''
N = int(input())
list = list(map(int,input().split()))
for i in list:
    if i%6 == 0:
        print('{:>1}'.format(i),end=' ')

