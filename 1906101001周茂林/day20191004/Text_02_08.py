a,b = map(str,input().split())
a = list(a)
c = len(a)
d = 1
e = 0
while d <= c:
    e += (int(b)**(d-1)*int(a[-d]))
    d = d+1
print(e)