#化为最简分式
def zdgys(a,b):
    if a%b == 0:
        return b
    else:
        return zdgys(b,a%b)
a,b = map(int,input('请输入一个分数：').split('/'))
x = a/zdgys(a,b)
y = b/zdgys(a,b)
print('该分数的最简式为%d/%d' % (x,y))
