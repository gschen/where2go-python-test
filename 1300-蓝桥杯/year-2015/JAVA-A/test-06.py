import math

def juli(w,m,n):
    ans=int(abs(math.ceil(m*1.0/w)-math.ceil(n*1.0/w)))
    if math.ceil(m*1.0/w)%2==0:
        mc=int(math.ceil(m*1.0/w)*w-m)
    else:
        mc=int(w-(math.ceil(m*1.0/w)*w-m)-1)
    if math.ceil(n*1.0/w)%2==0:
        nc = int(math.ceil(n * 1.0 / w) * w - n)
    else:
        nc=int(w-(math.ceil(n*1.0/w)*w-n)-1)
    return ans+abs(nc-mc)
print(juli(6,8,2))




