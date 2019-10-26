# 1
cm = input()
cm = float(cm)/100
feet = cm/0.3048
inch = (feet-int(feet))*12
inch = int(inch)
feet = int(feet)
print(feet,inch)

# 2
n,p=map(int,input().split())
m=(n%10+int(n/10)%10*10)
hour=int(n/100)
sum=hour*60+m+p
hour=int(sum/60)
m=sum-hour*60
print("%d%02d"%(hour,m))

# 3
n = int(input())
m = n%10*100+int(n/10)%10*10+int(n/100)
print(m)

# 4
x=int(input())
m=x%16
n=int(x/16)*10+m
print(n)

# 5
print("------------------------------------")
print("Province      Area(km2)   Pop.(10K)")
print("------------------------------------")
print("Anhui         139600.00   6461.00")
print("Beijing        16410.54   1180.70")
print("Chongqing      82400.00   3144.23")
print("Shanghai        6340.50   1360.26")
print("Zhejiang      101800.00   4894.00")
print("------------------------------------")

# 6
f1,a,c,f2=map(str,input().split())
f1=float(f1)
a=int(a)
c==str(c)
f2=float(f2)
print("%c %d %.2f %.2f"%(c,a,f1,f2))

# 7
a,b=map(str,input().split(':'))
a=int(a)
b=int(b)
am="AM"
pm="PM"
if a>12:
    a=a%12
    print("%d:%d %s"%(a,b,pm))
elif a==0:
    print("%d:%d %s"%(a,b,am))
elif a>0 and a<12:
    print("%d:%d %s"%(a,b,am))
else :
    print("%d:%d %s"%(a,b,pm))


