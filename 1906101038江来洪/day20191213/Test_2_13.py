#分段计算居民水费
x = int(input('请输入你的水费：'))
def function(x):
    if x<=15:
        return 4*x/3
    else:
        return 2.5*x-17.5
y = function(x)
print('%.2f'% y)