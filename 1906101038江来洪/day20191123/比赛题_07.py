#找出输入数组中连续三个数字平方和个最大值
def jiang(x):
    return x**2
N = int(input())
list = list(map(int,input().split()))
list1 = []
for i in range(N-2):
    s = 0
    s = s+jiang(list[i])+jiang(list[i+1])+jiang(list[i+2])
    list1.append(s)
print(max(list1))