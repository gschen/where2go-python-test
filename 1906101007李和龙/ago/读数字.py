dic = {'0':'ling','1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu'}
a = input()
for i in range(len(a)-1):
    if i == 0 and a[i] == '-':
        print('fu',end=' ')
    else:
        print(dic[a[i]],end=' ')
print(dic[a[-1]])

