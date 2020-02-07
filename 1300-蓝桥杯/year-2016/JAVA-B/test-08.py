n = int(input("n:"))
A = list(map(int, input().split(' ')))
B = []

for i in range(n):#遍历每一个数字
    zj = {A[i]}#用来存中间数字的集合(利用集合中的元素不能重合)
    if -A[i] not in B:# 如果第一次出现就直接将相反数保存到B
        B.append(-A[i])
    else:
        for j in range(i-1, -1, -1):# 如果曾经出现过就寻找之间的数字种类
            zj.add(A[j])
            if A[j] == A[i]:
                B.append(len(zj) - 1)
                break

print(B)
