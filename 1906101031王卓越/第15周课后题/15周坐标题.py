#15周课堂作业
def raw(l,n,q,k):
    if q<len(l):
        a=l[q][0]-l[n][0]
        b=l[q][1]-l[n][1]
        if abs(a)>abs(b) and q<len(l):
            k=k+abs(a)
            return raw(l,n+1,q+1,k)
        elif abs(b)>abs(a) and q<len(l):
            k=k+abs(b)
            return raw(l,n+1,q+1,k)
        elif abs(b)==abs(a) and q<len(l):
            k=k+abs(b)
            return raw(l,n+1,q+1,k)
        elif q==len(l)-1 :
            return k
    return k
l=eval(input('请输入：')
n=0
q=1
k=0
print(raw(l,n,q,k))