a = input()
b = list(input())
c = len(b)
n = c
for i in b[::-1]:
    n -= 1
    if i == a:
        print('index = {}'.format(n))
        break
    if n ==0:
        print('Not Found')