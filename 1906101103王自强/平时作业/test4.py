def fun(iterable):
    def rename(x):
        l_1=list(x.upper())
        l_2=list(x.lower())
        l_2[0]=l_1[0]
        o=''
        for i in l_2:
            o+=i
        return o
    return list(map(rename,iterable))