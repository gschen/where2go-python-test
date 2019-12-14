N,M,L=map(int,input('请分别输入三个值：').split())
l=list(input('请输入一串数字：').split())
s=[]
print(l,type(l))
for i in l:
    i=int(i)
    if M==2:
        if L==2:
            s.append(i)
        if L==8:
            int('i',2)
            s.append(int(oct(i)[2:]))
        if L==10:
            int('i',2)
            s.append(i)
    if M==8:
        if L==2:
            int('i',8)
            s.append(int(bin(i)[2:]))
        if L==8:
            s.append(i)
        if L==10:
            int('i',8)
            s.append(i)
    if M==10:
        if L==2:
            s.append(int(bin(i)[2:]))
        if L==8:
            s.append(int(oct(i)[2:]))
        if L==10:
            s.append(i)
print(max(s),min(s),s)

            
        


