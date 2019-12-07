lis = list(map(int, input().split()))
a, b, c = ((lis[0]-lis[2])**2 + (lis[1]-lis[3])**2)**0.5,\
    ((lis[0]-lis[4])**2 + (lis[1]-lis[5])**2)**0.5,\
    ((lis[4]-lis[2])**2 + (lis[5]-lis[3])**2)**0.5
if a+b > c and a+c > b and b+c > a:
    if a == b or a == c or b == c:
        print('IT', end=' ')
    else:
        print('T', end=' ')
    p = (a+b+c) / 2
    print('{:.2f}'.format((p*(p-a)*(p-b)*(p-c))**0.5))
else:
    print('NT')
