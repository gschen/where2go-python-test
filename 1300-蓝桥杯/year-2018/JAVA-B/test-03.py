
def fushumi(a,b,c,d):
    count=1
    sb=0
    xb=0
    while count<123456:
        sb=(a*c-b*d)
        xb=(b*c+a*d)
        c=sb
        d=xb
        count+=1
    return sb,"",xb,'i'
print(fushumi(2,3,2,3))

