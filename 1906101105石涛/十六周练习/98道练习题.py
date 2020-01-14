# coding=utf-8

#https://pintia.cn/problem-sets/1111652100718116864/problems/type/7（题的网址）

#1-1(1)
'''本题目要求读入2个整数A和B，然后输出它们的和。
输入格式:
在一行中给出一个被加数
在另一行中给出一个加数
输出格式:
在一行中输出和值。'''
# x=int(input())
# y=int(input())
# print(x+y)

#1-2(2)
'''在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
输入格式:
在一行中输入三个数。
输出格式:
在一行中输出公式值。'''
# l=input().split(' ')
# print(int(l[1])**2-4*int(l[0])*int(l[2]))

# 1-3(3)
# s="人生苦短，我学Python"
# print(s.encode("utf-8"))

# 2-1(4)
'''输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值。
输入格式:
在一行输入一个正整数m。
输出格式:
在一行中按照格式“sum = S”输出对应的和S.'''
# s=int(input('s='))
# m=0
# for i in range(11,(s+1)):
#     m+=i
# print(m)

# 2-2(5)
'''本题目要求计算下列分段函数f(x)的值：
x!=,y=1/x
x=0,y=0
输入格式:
输入在一行中给出实数x。'''
# x=int(input())
# if x!=0:
#     print('f(%.2f)=%.2f' % (x,1/x))
# else:
#     print('f(%.2f)=0.0' % x)

# 2-3(6)
'''为了提倡居民节约用电，某省电力公司执行“阶梯电价”，安装一户一表的居民用户电价分为两个“阶梯”：
月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；超过50千瓦时的，超出部分的用电量，
电价上调0.05元/千瓦时。请编写程序计算电费。'''
# x=int(input())
# if x<0:
#     print("Invalid Value!")
# elif x>0 and x<=50:
#     print('cost=%.1f' % (x*0.53))
# elif x>50:
#     print('cost=%.1f' % (x*0.53+(x-50)*0.58))

# 2-4(7)
'''
给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和
输入格式：a n
'''
# l=input().split()
# s,k=0,int(l[1])
# while k>0:
#     s+=int(l[0]*k)
#     k-=1
# print('s=%d' % s)

# 2-5(8)
'''本题要求编写程序，计算序列 1 + 1/3 + 1/5 + ... 的前N项之和'''
# n=int(input('求前几个项的和：'))
# l=[i for i in range(1,2*n)][::2]
# print(l)
# sum=0
# for i in l:
#     sum+=(1/int(i))
# print('%.6f' % sum)

# 2-6(9)
'''本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。'''
# n=int(input('N='))
# l=[i for i in range(1,2*n)][::2]
# sum=0
# x,y=1,0
# for i in l:
#     sum+=(y+1)/(int(i))*(-1)**(x+1)
#     # print('%d/%d' % ((y+1)*(-1)**(x+1)),(int(i)))
#     x+=1
#     y+=1
# print('%.3f' % sum)

# 2-7(10)
'''读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A
输入格式:
在一行中输入A和B(如：3,4)。
输出格式:
在一行中输出整数AA...A,一共B个A'''
# x=input().split(',')
# # print(x)
# m,n=x[0],int(x[1])
# print(m*n)

# 2-8(11)
'''输入一个整数和进制，转换成十进制输出'''
# # x=int('41',5)
# # print(x)
# x=input().split(',')
# print(int(x[0],int(x[1])))

# 2-9(12)
'''本题要求将输入的任意3个整数从小到大输出。
输入格式:
输入在一行中给出3个整数，其间以空格分隔。
输出格式:
在一行中将3个整数从小到大输出，其间以“->”相连。'''
# l=input().split()
# print(l)
# li,lis=[],[]
# for i in l:
#     li.append(eval(i))
# li.sort()
# for x in li:
#     lis.append('->%d' % x)
# print(lis)
# print(''.join(lis)[2:])

# 2-10(13)
'''输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
温度转换的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。
输入格式:
在一行中输入2个整数，分别表示lower和upper的值，中间用空格分开。
输出格式:
第一行输出："fahr celsius"
接着每行输出一个华氏温度fahr（整型）与一个摄氏温度celsius（#占据6个字符宽度，靠右对齐，保留1位小数#）。
若输入的范围不合法，则输出"Invalid."。 '''
# a,b=map(int,input().split())
# if b>a and b<100:
#     print('fahr celsius')
#     for i in range(a,b+1,2):
#         print('{}{:>6.1f}'.format(i,(i-32)*5/9))
# else:
#     print("Invalid.")

# 2-11(14)
'''本题要求对两个正整数m和n（m≤n）编写程序，计算序列和m^2+1/m+(m+1)^2+1/(m+1)+⋯+n^2+1/n。
输入格式:
输入在一行中给出两个正整数m和n（m≤n），其间以空格分开。
输出格式:
在一行中按照“sum = S”的格式输出部分和的值S，精确到小数点后六位。题目保证计算结果不超过双精度范围。'''
# m,n=map(int,input().split())
# sum=0
# for i in range(m,n+1):
#     sum+=i**2+1/i
# print('%.6f' % sum)

# 2-12(15)
'''本题要求编写程序，根据输入的三角形的三条边a、b、c，计算并输出面积和周长。注意：在一个三角形中，
 任意两边之和大于第三边。三角形面积计算公式：area=(s(s−a)(s−b)(s−c))**0.5
​，其中s=(a+b+c)/2。
输入格式：
输入为3个正整数，分别代表三角形的3条边a、b、c。
输出格式：
如果输入的边能构成一个三角形，则在一行内，按照
area = 面积; perimeter = 周长
的格式输出，保留两位小数。否则，输出
These sides do not correspond to a valid triangle'''
# a,b,c=map(int,input().split())
# s=(a+b+c)/2
# if a+b>c and a+c>b and b+c>a:
#     print('area=%.2f,perimeter=%.2f' %(((s*(s-a)*(s-b)*(s-c))**0.5),2*s))
# else:
#     print('These sides do not correspond to a valid triangle')

# 2-13(16)
'''为鼓励居民节约用水，自来水公司采取按用水量阶梯式计价的办法，居民应交水费y（元）与月用水量x（吨）相关：
当x不超过15吨时，y=4x/3；超过后，y=2.5x−17.5。请编写程序实现水费的计算。
输入格式：
输入在一行中给出非负实数x。
输出格式：
在一行输出应交的水费，精确到小数点后2位。'''
# x=int(input())
# if x<=15:
#     y=4*x/3
# else:
#     y=2.5*x-17.5
# print('%.2f'%y)

# 2-14(17)
'''给定两个整数A和B，输出从A到B的所有整数以及这些数的和。
输入格式：
输入在一行中给出2个整数A和B，其中−100≤A≤B≤100，其间以空格分隔。
输出格式：
首先顺序输出从A到B的所有整数，每5个数字占一行，每个数字占5个字符宽度，向右对齐。最后在一行中按Sum = X的格式输出全部数字的和X'''
