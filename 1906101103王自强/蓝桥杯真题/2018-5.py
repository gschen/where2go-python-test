'''螺旋折线
对于整点(X, Y)，我们定义它到原点的距离dis(X, Y)是从原点到(X, Y)的螺旋折线段的长度。  
例如dis(0, 1)=3, dis(-2, -1)=9  
给出整点坐标(X, Y)，你能计算出dis(X, Y)吗？
【输入格式】
X和Y 
对于40%的数据，-1000 <= X, Y <= 1000  
对于70%的数据，-100000 <= X， Y <= 100000  
对于100%的数据, -1000000000 <= X, Y <= 1000000000  
【输出格式】
输出dis(X, Y)  
【输入样例】
0 1
【输出样例】
3'''
x,y=map(int,input().split(' '))
n=max(abs(x),abs(y))
if x==-n:
    sum=abs(-n-y)
if x==n:
    sum=abs(n-y)+4*n
if y==n:
    sum=abs(-n-x)+2*n
if y==-n:
    sum=abs(-n-x)+6*n
for i in range(1,n):
    sum+=8*i
print(sum)