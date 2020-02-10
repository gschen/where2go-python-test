a = int(input())

A = []

while a >0:
    if a % 26 == 0 :
        b = 26+64
        A.append(b)
        a//=26
        a = a-1
    else:
        b =a%26+64
        A.append(b)
        a //= 26

str = ''
for i in range(len(A)):
    str =str + chr(A[len(A)-i-1])
print(str)