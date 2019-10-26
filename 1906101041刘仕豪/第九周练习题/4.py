'''
4、	斐波那契数列。（斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。前两项相加等于第三项）
'''
#def fib(n):

n = int(input("请输入你想得到的第几项数："))
a,b = 0,1
t = 0
while t<n-2:
    a,b = b,a+b
    t+=1
if n ==1:
    b = 0
print(b)
