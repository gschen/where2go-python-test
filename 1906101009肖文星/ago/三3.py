'''一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''
a=input()
if a[0:1]==a[-1:] and a[1:2]==a[-2:-1]:
    print(True)
else:
    print(False)