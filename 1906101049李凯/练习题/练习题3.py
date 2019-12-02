s=0
a=1
b=2
for i in range(1,21):
    s=s+b/a
    b,a=a+b,b
    print(s)