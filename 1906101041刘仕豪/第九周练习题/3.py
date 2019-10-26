'''
3、	输入三个整数x,y,z，请把这三个数由小到大输出。
'''
x = int(input("请输入正整数x："))
y = int(input("请输入正整数y："))
z = int(input("请输入正整数z："))
if y>x and y>z and z>x:
    x1 = y
    y1 = z
    z1 = x
elif y>x and y>z and x>z:
    x1 = y
    y1 = x
    z1 = z
elif x>z and z>y:
    y1 = z
    z1 = y
    x1 = x
elif z>x and x>y:
    x1 = z
    y1 = x
    z1 = y
elif z>y and y>x:
    x1 = z
    z1 = x
    y1 = y
print("正整数x,y,z从小到大排序为{}<{}<{}".format(z1,y1,x1))