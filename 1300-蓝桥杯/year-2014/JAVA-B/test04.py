'''
6.标题：奇怪的分式
'''
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def judge(a,b,c,d):
    x1=a*c
    y1=b*d
    g=gcd(x1,y1)
    x1=x1/g
    y1=y1/g

    x2=10*a+c
    y2=10*b+d
    g=gcd(x2,y2)
    x2=x2/g
    y2=y2/g
    if x1==x2 and y1==y2:
        return True
    return False

res=0
for i in range(10):
    for j in range(10):
        for a in range(10):
            for b in range(10):
                if i!=j and a!=b:
                    if judge(i,j,a,b):
                        res+=1
print(res)