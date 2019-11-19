'''求1+2!+3!+...+20!的和。'''
a = 0
c = 1
for b in range(1,21):
    c = c * b
    a += c
print(a)