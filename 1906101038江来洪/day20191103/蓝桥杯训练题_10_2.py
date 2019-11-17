#最后留下的是原来几号
n = int(input('请输入人数：'))
list = list(range(1,n+1))
if n == 1:
    print('最后留下来的是：1')
else:
    x = 0
    for i in range(n-1):
        x = (x+3)%len(list)-1
        list.pop(x)
        if x < 0:
            x = 0
    print('最后留下来的是：',list[0])
