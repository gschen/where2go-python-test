'''斐波那契数列。（斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。前两项相加等于第三项）求前101项'''
a=0
b=1
for i in range(99):
    c=a+b
    a,b=b,c
    print(c)