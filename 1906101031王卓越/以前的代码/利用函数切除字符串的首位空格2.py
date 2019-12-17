def raw(n):
    for i in n:
        for k in n[:-1]:
            if i!=" " and k!=" ":
                return n[n.index(i):len(n)-n.index(k)+2]#len表示字符串内所有的字符串数目包括空格
print(raw('       12yhuihyu       '))#index查找（）内的值在字符串中的位置
#王卓越             