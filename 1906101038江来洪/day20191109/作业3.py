#用切片方法切出首尾没有空格的字符串
def jiang1(x):
    for m in x:
        for n in x[::-1]:
            if m != ' ' and n != ' ':
                return x[x.index(m):len(x)-x[::-1].index(n)]
x = input('请输入一个字符串：')
print(jiang1(x))