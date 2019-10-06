n = eval(input())
s = 0
for a in range(0,n+1):
    s = s+((-(-1)**a)*((a)/(2*a-1)))
print("%.3f" %(s))
