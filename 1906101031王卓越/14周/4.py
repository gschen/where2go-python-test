def raw(N):     
    if N>=11:
        print(11)
        return raw(N-11)
    elif 5<=N<11:
        print(5)
        return raw(N-5)
    elif 2<=N<5:
        print(2)
        return raw(N-2)
    elif 1<=N<2:
        print(1)
N=int(input('请输入N<=10000:'))
raw(N)
# N=int(input('请输入N<=10000:'))
# while True:
#     if N>=11:
#         N=N-11
#         print(11)
#     elif 5<=N<11:
#         N=N-5
#         print(5)
#     elif 2<=N<5:
#         N=N-2
#         print(2)
#     elif 1<=N<2:
#         N=N-1
#         print(1)
#     elif N==0:
#         break







         
