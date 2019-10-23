import re
x,y,z =re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
x,y,z =int(x),int(y),int(z)
a=max(x,y,z)
b=min(x,y,z)
print(b,x+y+z-a-b,a)