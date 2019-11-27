def raw(l):
    for i in range(0,8):
        l.append(l[-1]*l[-2])
        if i==7:
            p=tuple(l)
            print(p)
    return
l=[1,2]
raw(l)
#王卓越