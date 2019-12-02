#不能用set()来解
l=map(int,input('请输入一个列表：').split())
n=0
for a in range(0,len(l)):
    for b in range(0,len(l)):
        if l[a]==l[b] and a!=b:           
            print(l,len(l))

    

