'''在二维平面上有无数个1x1的小方格。
我们以某个小方格的一个顶点为圆心画一个半径为1000的圆。
你能计算出这个圆里有多少个完整的小方格吗？
注意：需要提交的是一个整数，不要填写任何多余内容。'''
sum=0
for x in range(0,1001):
    for y in range(0,1001):
       sum+=1
print(sum*4)