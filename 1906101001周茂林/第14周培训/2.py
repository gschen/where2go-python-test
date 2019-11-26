'''
正整数分解
'''
def fenjie(n):
    lis = []
    for i in range(2,n+1):
        while n % i == 0:
            lis.append(i)
            n /= i
    return lis


n = int(input())
l = fenjie(n)
if len(l) > 1:
    print(n, '=', ' * '.join([str(x) for x in l]))
else:
    print(n, '=', n, '*', '1')