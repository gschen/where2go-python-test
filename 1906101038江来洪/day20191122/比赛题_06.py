#找出输入数组中连续三个数字都是素数的组数
N = int(input())
list = list(map(int,input().split()))
def sushu(x):
    if x == 0 or x == 1:
        return 1
    else:
        k = 0
        for i in range(2,x):
            if x%i == 0:
                k += 1
        if k == 0:
            return 1
        else:
            return 0
s = 0
for i in range(N-2):
    if sushu(list[i]) + sushu(list[i+1]) + sushu(list[i+2]) == 3:
        s += 1
print(s)