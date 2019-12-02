a,b=map(int,input().split())
s=0
while a<=b:
    for i in range(5):
        print('{:>5}'.format(a),end='')
        s=s+a
        a+=1
        if a>b:
            break
    print()
print("sum = %d"%s)