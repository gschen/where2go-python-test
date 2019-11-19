'''
判断101-200之间有多少个素数，并输出所有素数。
'''
n = 0
for i in range(101,201):
    for a in range(2,i):
        if i % a == 0: 
            break
    else:
        print(i)
        n = n + 1
print('101-200之间有{}个素数'.format(n))