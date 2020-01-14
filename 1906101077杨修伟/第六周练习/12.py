#huashi,sheshi
a,b=input().split()
a,b=eval(a),eval(b)
if(a>b):
    print("Invalid.")
else:
    print("fahr celsius")
    i = a
    while i <= b:
        print("{:d}{:>6.1f}".format(i,5*(i-32)/9))
        i += 2