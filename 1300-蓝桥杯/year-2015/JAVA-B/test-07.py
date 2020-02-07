#骰子问题
n, m = input().split()
def touzi(n,m):
    lis=[]
    for i in range(eval(m)):
        lis.append(list(map(int, input().split(','))))# 用列表将对应的骰子存起来


