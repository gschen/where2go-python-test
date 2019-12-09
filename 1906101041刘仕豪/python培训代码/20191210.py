# #1
# a = int(input())
# b = int(input())
# print(a+b)

# #2
# a,b,c = map(int,input().split())
# print(b*b - 4*a*c)

# #3
# s = '人生苦短，我学python'
# print(s.encode('utf-8'))

# #4
# m = int(input())
# t = 11
# s = 0
# while m >= t:
#     s += t
#     t += 1
# print('sum =',s)

# #5
# x = float(input())
# if x != 0:
#     print('f(%.1f) = %.1f'%(x,1/x))
# else:
#     print('f(0.0) = 0.0')

# #6
# n = int(input())
# if n >= 0 and n <= 50:
#     print('cost = %.2f'%(n*0.53))
# elif n > 50:
#     print('cost = %.2f'%(n*0.53+(n-50)*0.05))
# else:
#     print('Invalid Value!')

# #7
# a,n = map(int,input().split())
# t = 0
# s = 0
# b = a
# while n > t:
#     s += a
#     a = a*10+b
#     t += 1
# print('s =',s)

# #8
# N = int(input())
# t = 0
# s = 0
# while N > t:
#     t += 1
#     s += 1/(2*t-1)
# s = str(s)
# s = s[:8]
# s = float(s)
# print('sum =',s)

# #9
# N = int(input())
# t = 0
# s = 0
# while N > t:
#     t += 1
#     s += t/(2*t-1)*(-1)**(t+1)
# print('%.3f'%s)

# #10
# A,B = map(int,input().split(','))
# A = str(A)
# print(A*B)

# #11
# m,n = map(int,input().split(','))
# m = str(m)
# a = len(m) - 1
# s = 0
# for i in m:
#     s += int(i)*(n**a)
#     a -= 1
# print(s)




























# #89
# s = list(input().split('.',',',' ','\n','...',':',';'))
# dic = {}
# for i in s:
#     s = s.lower()
#     s = s[0:15]
#     if i not in dic:
#         dic.update(i = 0)
#     if i in dic:
#


