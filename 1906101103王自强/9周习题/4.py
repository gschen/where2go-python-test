while True:
    n = int(input('请输入你要求的项数:'))
    n2 = 0
    n1 = 1
    x = 0
    for i in range(2, n + 1):
        x = n2 + n1
        n2 = n1
        n1 = x
        print('第{}项数是{}'.format(n, x))
        #4