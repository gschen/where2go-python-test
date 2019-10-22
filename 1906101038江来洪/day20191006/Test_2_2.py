#计算一个分段函数
x = int(input('请输入一个数：'))
def function(x):
    if x == 0:
        return 0
    else:
        return 1/x
y = function(x)
print('f(%s) =' % ('%.1f' % x), '%.1f'% y)