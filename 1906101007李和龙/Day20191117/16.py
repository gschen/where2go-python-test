a=['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
s=input()
l=len(s)
for i in range(1,l):
    if s[i-1:i+2]in a:
        print(s[i-5:i+2])
    else:
        print('2000Jan')