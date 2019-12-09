def huax(h, l):
    # h, l = map(int, input().split())
    lis = list([' ' for i in range(h+l-1)] for x in range(h))
    for i in range(h):
        lis[i][i:i+l] = '*' * l
        lis[i][-1 - i:-1 - i - l:-1] = '*' * l
    for minil in lis:
        print(''.join(minil))


huax(14, 5)
huax(7, 8)
huax(18, 2)
huax(11, 4)