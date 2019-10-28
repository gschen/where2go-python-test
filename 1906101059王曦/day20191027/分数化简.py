n,m =input().split("/")
n=int(n)
m=int(m)
for i in range(2,n):
        while n%i == 0 and m%i == 0:
            n = n//i
            m = m//i
print(str(n)+"/"+str(m))