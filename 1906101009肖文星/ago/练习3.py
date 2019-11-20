'''输入三个整数x,y,z，请把这三个数由小到大输出。'''
x = int(input('第一个整数x：'))
y = int(input('第二个整数x：'))
z = int(input('第三个整数x：'))
if x > y:
   y,x=x,y
if x>z:
    z,x=x,z
if y>z:
    z,y=y,z
print(x, y, z)
