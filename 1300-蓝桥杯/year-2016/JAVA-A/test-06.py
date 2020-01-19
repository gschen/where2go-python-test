n=input("输入：")
a=0
b=0
# f=[3]
# sum=[]

f=[3]
for i in range(0,3):
    f[i]=input()
n=[]
for j in range(0,5):
    n[j]=input()
while n>f[0]:
    if a==0:
        if n>=f[2] and f[2]%2==1:
            a=1
            n-=f[2]
        elif n>f[1] and f[1]%2==1:
            a=1
            n-=f[1]
        elif n>=f[0] and f[0]%2==1:
            a=1
            sum-=f[0]
        else:
            n-=f[0]
    elif a==1:
        if n>=f[2] and f[2]%2==1:
            n-=f[2]
        elif n>f[1] and f[1]%2==1:
            n-=f[1]
        elif n>=f[0] and f[0]%2==1:
            sum-=f[0]
        elif n>=f[0]:
            a=0
            n-=f[0]
    if b==0:
        if n>=f[2] and f[2]%2==1:
            b=1
            n-=f[2]
        elif n>f[1] and f[1]%2==1:
            b=1
            n-=f[1]
        elif n>=f[0] and f[0]%2==1:
            b=1
            sum-=f[0]
        elif n>=f[0]:
            n-=f[0]
    elif b==1:
        if n>=f[2] and f[2]%2==1:
            n-=f[2]
        elif n>f[1] and f[1]%2==1:
            n-=f[1]
        elif n>=f[0] and f[0]%2==1:
            sum-=f[0]
        elif n>=f[0]:
            b=0
            n-=f[0]
    if a==b:
        print("0")
    elif a<b:
        print("-")
    else:
        print("+")
    if i!=4:
        print("")
