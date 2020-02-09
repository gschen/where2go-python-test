'''
5. 现知道有些数为回文数，
例如121，242，12321。
我们就称这种数字为回文数，像10，14，467就不为回文数。
先要求你用程序将区间[1，100000]内所有的回文数输出。
'''
# l=[]
# for num in range(1,100000):
#     y=str(num)
#     if len(y)==3:
#         if y[0]==y[-1] and y[1]==str((int(y[0])+1)) and y[0]<y[1]:
#             k=''.join(y)
#             l.append(k)
#     elif len(y)==5:
#         if y[0]==y[-1] and y[1]==y[-2] and y[2]==str((int(y[1])+1)) and y[0]<y[1]and y[1]==str((int(y[0])+1)):
#             k=''.join(y)
#             l.append(y)
# for ccc in l:
#     print(ccc)


for i in range(1,100000):
    if i==int(str(i)[::-1]):
        print(i)