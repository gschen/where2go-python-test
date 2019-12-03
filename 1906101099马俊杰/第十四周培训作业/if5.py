def chk(s):
    return s[::-1] == s
for i in range(1,10000):
    if (chk(str(i))):
        print(i)