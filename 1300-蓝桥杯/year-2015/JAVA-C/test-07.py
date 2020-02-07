h=eval(input())
w=eval(input())
h1=h//2
for i in range(0,h1-1):
    s=str('.'*i+'*'*w+'.'*((h1-2-i)*2+1)+'*'*w)
    print(s)
s1 = str('.' * (h1) + '*' * (w))
print(s1)


for i in range(h1-2,-1,-1):
    s = str('.' * i + '*' * w + '.' * ((h1 - 2 - i) * 2 + 1) + '*' * w)
    s1=str('.'*(h1-i-2)+'*'*w+'.'*((i*2)+1)+'*'*w)
    print(s)
