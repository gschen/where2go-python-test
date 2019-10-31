#转换函数的使用
a,b = map(int,input('请输入两个数：').split(','))
a = str(a)
b = int(b)
c = int(a,b)
print(c)