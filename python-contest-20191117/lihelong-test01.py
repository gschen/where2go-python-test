str1 = input()
value = []
value2 =[]
key1 = []
q,w,e,r = 0,0,0,0
for i in str1:
    if i == "b":
        q += 1
    elif i == "m":
        w += 1
    elif i == "p":
        e += 1
    elif i == "t":
        r += 1
dict1 = {}
dict1["b"] = q
dict1["m"] = w
dict1["p"] = e
dict1["t"] = r

for m in dict1.values():
    value.append(m)
value.sort()
yi = value[::-1][0]
er = value[::-1][1]
san = value[::-1][2]
si = value[::-1][3]
if yi!=er!=san!=si:
    for n in dict1.values():
        value2.append(n)
    weizhi1 = value2.index(yi)
    weizhi2 = value2.index(er)
    weizhi3 = value2.index(san)
    weizhi4 = value2.index(si)

    for k in dict1.keys():
        key1.append(k)
    print((key1[weizhi1]),yi)
    print((key1[weizhi2]),er)
    print((key1[weizhi3]),san)
    print((key1[weizhi4]),si)
elif yi == er:
    sorted()
