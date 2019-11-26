def addMulti(*n):
    s=0
    for i in n: 
        s = i**2 + s
    return s
print(addMulti(1,2,3))
#王卓越