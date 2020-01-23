s=[]
for n in range(99):
    for o in range(99):
        for m in range(99):
            a=3**n*5**o*7**m
            s.append(a)
s.sort()
for i in range(len(s)):
    if s[i]==59084709587505:
        print(i)
