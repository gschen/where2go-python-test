'''
3.有一个数列（1，2，3，6，……），第一项为1，第二项为2，第三项为前面两项的乘积，请使用生成器，并且打印出前10项。
'''
def nnn(m):
    n,a,b,c = 0,1,2,3
    while n < m:
        yield a
        a,b,c = b,c,b*c
        n += 1
    return 'done'
for n in nnn(10):
    print(n)