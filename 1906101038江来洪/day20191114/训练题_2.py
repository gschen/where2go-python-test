#小明走39级台阶，每步只迈1到2级台阶，最后共走了偶数步，计算出刚好走完39级台阶的所有情况
def jiec(y):
    if y == 1 or y == 0:
        return 1
    else:
        return y*jiec(y-1)
def jiang1(a,x):
    s = 1
    for i in range(a):
        s = s*x
        x-=1
    return s
def jiang(x):
    a = 39-x
    y = 39-x
    return jiang1(a,x)/jiec(y)
S = 0
for x in range(20,40,2):
    S = S+jiang(x)
print(S)
