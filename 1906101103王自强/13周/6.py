'''.对于给出的长度为N的整数数组，对连续3个元素求平方和,输出平方和的最大值。
输入说明:第-行,数组中元素个数N(N< 1000),第二行是这个数组中的N个元素，间用空格隔开,每个元素小于100000.
输出说明:输出连续3个元素平方和的最大值。
输入样例: 8
1 1 -1 2 -3 3 -4 2
输出样例: 34
'''
N=int(input())
l=list(input().split(' '))
box=[]
for i in range(N-2):
    a=int(l[i])**2+int(l[i+1])**2+int(l[i+2])**2
    box.append(a)
print(max(box))