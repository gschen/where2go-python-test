'''将一个整数数组中的偶数按输入次序输出。
输入说明:第一行是整数N (N<10000) , 表示数组中的元素个数，第二 _行是这个数组中的N个元素,规定元素中至少包含-一个偶数。
输出说明:输出数组中的偶数，如果有两个以上的偶数，中间用空格隔开。
输入样例: 7
1 2 3 6 9 11 17
输出样例: 2 6
'''
N=int(input())
l=list(input().split(' '))
m=''
for i in l:
    if int(i)%2==0:
        m+=i+' '
print(m)