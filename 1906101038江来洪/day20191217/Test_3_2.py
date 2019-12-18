#查验身份证是否是正确的
N = int(input('请输入你要查验身份证的个数：'))
list1 = []
list2 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
list3 = [1,0,'x',9,8,7,6,5,4,3,2]
for i in range(N):
    n = int(input('请输入你要查验的身份证号码：'))
    for a in range(2,19):
        m = (n%(10**a))//(10**(a-1))
        s = n%10
        a += 1
        list1.append(m)
    list1.reverse()
    S = 0
    for k in range(17):
        S += list1[k]*list2[k]
    z = S%11
    z = int(z)
    if z != s:
        print('该身份证是错的')
    else:
        print('该身份证是对的')
    list1 = []






