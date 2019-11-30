'''
证明在偶数n以内，歌德巴赫猜想是成立的。
歌德巴赫猜想是：任何一个充分大的偶数都可以表示为两个素数之和。
例如,4=2+2   6=3+3   8=3+5  50=3+47。
【输入形式】
输入偶数n
【输出形式】
对每一个偶数4, 6, 8, ..., n，依次输出一行。该行内容是<偶数>=<素数1>+<素数2>，要求素数1<=素数2.
【样例输入】
6
【样例输出】
4 = 2 + 2
6 = 3 + 3
'''
def gedebahe(N):
    lis = []
    for i in range(2, N):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lis.append(i)
    for i in range(4, N+1, 2):
        for m in lis:
            print('[[[', m)
            for n in lis:
                if m <= n and m + n == i:
                    print(i, '=', m, '+', n)
                    break
            else:
                continue
            break


gedebahe(int(input('输入偶数：')))
