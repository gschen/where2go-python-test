x='abcd'
n=0
for q in x:
    for w in x:
        for e in x:
            if q != w and q != e and w != e:
                n=n+1
                print(q,w,e)
print("一共有{:.2f}个".format(n))