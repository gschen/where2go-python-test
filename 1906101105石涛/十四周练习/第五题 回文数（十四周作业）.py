# coding=utf-8
'''5. 现知道有些数为回文数，例如121，242，12321。我们就称这种数字为回文数，像10，14，467就不为回文数。先要求你用程序将区间[1，100000]内所有的回文数输出。'''
print('以下为100000所有的回文数：')
print()
l=[]
L=[]
for i in range(1,100000):
    l.append([str(i)])
# print(l)
for i in l:
    # x=len([x for x in str(' '.join(i))])
    # print(x)
    for ii in i[0][0]:
        # print(ii)
        for iii in i[0][-1]:
            # print(iii)
            if ii==iii and len([x for x in ' '.join(i)])<=2:
                L.append(i)
            elif ii==iii and len([x for x in ' '.join(i)])>=3:
                for m in [i]:
                    for mm in m[0][1]:
                        for mmm in m[0][-2]:
                            if mm==mmm and len([x for x in ' '.join(m)])<=5:
                                L.append(m)
                            elif mm==mmm and len([x for x in ' '.join(m)])>=6:
                                for n in [m]:
                                    for nn in m[0][2]:
                                        for nnn in m[0][-3]:
                                            if nn==nnn:
                                                L.append(n)
print(L)