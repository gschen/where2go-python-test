# s1=eval(input())
# s2=eval(input())
# # print(s1+s2)
#
# a,b,c=map(int,input().split())
# k=b*b-4*a*c
# print(k)

# s = "人生苦短，我学Python"
# print(s.encode("utf-8"))


# m=int(input())
# S=0
# for i in range(11,m+1):
#     S=S+i
# print('sum=',S)
#
# x=eval(input())
# if x==0:
#     print('f(0.0)=0.0')
# else:
#     print('f({:.1f})={:.1f}'.format(x,1/x))

'''月用电量50千瓦时（含50千瓦时）以内的，电价为0.53元/千瓦时；
超过50千瓦时的，超出部分的用电量，电价上调0.05元/千瓦时。
# 请编写程序计算电费。'''
# x=eval(input())
# if x<=50 and x>=0:
#     y=0.53*x
# elif x>50:
#     y=0.53*50 +(x-50)*(0.53+0.05)
# else:
#     print("Invalid Value!")
# print('cost={:.2f}'.format(y))



#
# def s(a,n):
#     l= []
#     res = 0
#     a=str(a)
#     for i in range(1,n+1):
#         l.append(int(a*i))
#         print(l[i-1],end=" ")
#         if i<n:
#             print("+",end=" ")
#     for j in l:
#         res += j
#     print("=", res)
#     return res
# s(2,3)


# a,n=map(int,input().split())
# l=list()
# s=0
# a=str(a)
# for i in range(1,n+1):
#     l.append(a*i)
# for k in range(0,(len(l))):
#     s=s+int(l[k])
# print('s=',s)

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s+=1/(2*i-1)
# print('sum=%.6f' % s)

# n=eval(input())
# s1=0
# s2=0
# for i in range(1,n+1):
#     if i%2==0:
#         y1=-(i/(2*i-1))
#         s1+=y1
#     elif i%2!=0:
#         y2=i/(2*i-1)
#         s2+=y2
# print('{:.3f}'.format(s1+s2))
#
# A,B=map(int,input().split())
# A=str(A)*B
# print(int(A))

# n,j=map(int,input().split(','))
# l=str(n)
# y=0
# print(len(l))
# for i in range(len(l)):
#     y+=int(l[i])*(j**(len(l)-1-i))
# print(y)

# a,b,c=map(int,input().split())
# l=[a,b,c]
# l.sort()
# print('->'.join(str(ccc) for ccc in l))

'''C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。'''
# f,c=map(int,input().split())
# if f>c:
#     print('Invalid.')
# else:
#     print('fahr','celsius')
#     for i in range((int(c-f)//2)+1):
#         print('{}'.format(int(f+i*2)),'{:.1f}'.rjust(6).format((5*(int(f+i*2)-32))/9))




#
# '''本题要求对两个正整数m和n（m≤n）编写程序，计算序列和m
# ​2
# ​​ +1/m+(m+1)
# ​2
# ​​ +1/(m+1)+⋯+n
# ​2
# ​​ +1/n。'''
# m,n=map(int,in)