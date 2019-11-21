#将一个整数数组中的偶数按输入次序输出
n = int(input())
s = map(int,input().split())
list1 = list(s)
l = []
for i in list1:
    if i%2==0:
        l.append(i)
for i in l:
    print(i ,end=' ')