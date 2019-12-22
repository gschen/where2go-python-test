lower,upper=map(int,input().split(' '))
if lower<=upper<=100:
    print('fahr celsius')
    for i in range(lower,upper,2):
        print('{}{:>6.1f}'.format(i,5*(i-32)/9))
else:
    print("Invalid.")