n = int(input())
s = ''
lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while n > 26:
    m = n%26
    n = n//26
    if m != 0:
        s = lis[m-1]+s
    else:
        s = s +'Z'
s =lis[n-1] +s
print(s)