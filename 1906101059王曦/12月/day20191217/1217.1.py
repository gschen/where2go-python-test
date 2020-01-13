T= int(input())
dist,disw,tw,ttu,temp,tmp = 0,0,0,0,0,0
for i in range(0,T):
    if (i%90>=0 and i%90<10) or (i%90>=40 and i%90<50) or (i%90>=80 and i%90<90):
        dist += 9
if disw > dist:
    print("@_@ %d"%disw)
elif disw < dist:
    print("^_^ %d"%dist)
else:
    print("-_- %d"%disw)