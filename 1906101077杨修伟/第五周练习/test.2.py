x,y = map(int,input().split())
m=(x%10+int(x/10)%10*10)
hour = int(x/100)
sum=hour*60+m+y
hour=int(sum/60)
m=sum-hour*60
print("%d%02d"%(hour,m))

