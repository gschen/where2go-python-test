m, n = map(int,input('请分别输入起始时间和流逝时间：').split())
o = m%100
p = n%60
q = (o+p)%60
r = (o+n)//60
s = (m-o)+r*100+q
print(s)

    
    
    