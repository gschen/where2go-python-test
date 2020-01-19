x1,y1,x2,y2=input('请输入第一个矩形的左下坐标和右上坐标（用空格分开）：').split(' ')
x3,y3,x4,y4=input('请输入第二个矩形的左下坐标和右上坐标（用空格分开）：').split(' ')
lisx=[]
lisy=[]
for i in range(int(x1),int(x2)+1):
    for j in range(int(y1),int(y2)+1):
        for x in range(int(x3),int(x4)+1):
            for y in range(int(y3),int(y4)+1):
                if i==x and j==y:
                    lisx.append(i)
                    lisy.append(j)
if len(lisx)==0:
    print('不存在交集')
else:
    print(min(lisx),max(lisx),min(lisy),max(lisy))

