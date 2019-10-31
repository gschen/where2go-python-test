x,y=input('请输入一个分数：').split('/')
x=int(x)
y=int(y)
for i in range(2,x+1):
    if x%i==0 and y%i==0:
       x=int(x/i)
       y=int(y/i)
print('化简后为{}/{}'.format(x,y))
