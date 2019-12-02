a,b,c,d,sum,sum1=1,1,3,3,1,1
n = float(input())
while sum1 > n:
    sum1 = a / d
    sum = sum1 + sum
    b+=1
    c = c + 2
    a = a*b
    d = d * c
ans = sum*2
print("%.6f"%ans)