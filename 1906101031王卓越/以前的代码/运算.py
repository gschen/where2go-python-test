m, n = map(int,input('请分别输入：').split())
s = m
i = 1
b = 0
k = 0
while i < n:
    i = i + 1
    a=s
    s = s*10+m
    k=a+k
print(s + k)

 
        



