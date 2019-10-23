"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""
x,y,z = map(int,input().split())
while x > y and x >z:
    if y > z :
        x,y,z = x,y,z
    else:
        x,y,z = x, z, y
    break
while y > z and y >x:
    if x > z :
        x,y,z = y,x,z
    else:
        x,y,z = y,z,x
    break
while z > x and z >y:
    if y > x :
        x,y,z = z,y,x
    else:
        x,y,z = z,x,y
    break
print(z,y,x)

