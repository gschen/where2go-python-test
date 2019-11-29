def xuanren(n):
    l= list(range(1, n + 1))#先将给定的人创建成一个list
    t=0                     #添加一个统计变量，方便我们将需要剔除地人删掉
    while len(l)>1:         #
        l2=l[:]             #拷贝一个list，接下来可以通过条件移除之前list里面的元素
        for i in range(0, len(l2)):
            t+=1
            if t%3==0:          #计数器t没加三次就移除一个人
                l.remove(l2[i])
    return l[0]          #当只剩下最后一个人的时候返回序号 约瑟夫环算法









import time
p = time.time()



for a in range(1,10):
    for b in range(0,10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(1,10):
                    if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
                        if (e*10000+d*1000+c*100+b*10+a)%(a*10000+b*1000+c*100+d*10+e)==0:
                            print(a*10000+b*1000+c*100+d*10+e)



j = time.time()
print(j-p)










def zhiyinshu(a):
    l = list(range(1,a+1))
    l2 = []
    for i in l:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                l2.append(i)
    l2.insert(0,2)
    l3 = [a,'=']
    for i in l2:
        while a%i == 0:
            a = a/i
            l3.append(i)
            l3.append('*')
    l3.pop(-1)
    for j in l3:
        print(j,end='')
zhiyinshu(90)
