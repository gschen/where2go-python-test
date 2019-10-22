#计算用户的电费
x = int(input('请输入月用电量：'))
def function(x):
    if x <= 50:
        return 0.53*x
    else:
        return 0.53*50+(x-50)*(0.53+0.05)
y = function(x)
print('cost = %s' % '%.2f'% y)