# 在输入的数组中找出一对和为给定的目标值的数组下标
list = list(map(int,input('请输入一组数字：').split()))
target = int(input('确认你的目标值：'))
a = len(list)
for x in range(0,a):
    for y in range(0,x):
        if list[x]+list[y] == target:
            print('[%d,%d]' % (y,x))