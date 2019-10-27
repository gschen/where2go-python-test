n=input('请输入一个不超过5位数的整数：')
x=len(n)
y=list(n)
if x==5:
    z=y[4]+y[3]+y[2]+y[1]+y[0]
elif x==4:
    z=y[3]+y+[2]+y[1]+y[0]
elif x==3:
    z=y[2]+y+[1]+y[0]
elif x==2:
    z=y+[1]+y[0]
else:
    z=y[0]
print('你输入的是{}位数，倒叙过后是{}。'.format(x,z))
#12