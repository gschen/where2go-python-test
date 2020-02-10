a = input()
b = input()
A = []
B = []
for k in a:
    A.append(k)
for j in b:
    B.append(j)

C = []
panduanA = True
while len(A)!=0 and len(B)!=0:
    if panduanA==True:
        if A[0] in C:
            count = 0
            A.append(A[0])
            for i in range(len(C)-C.index(A[0])):
                A.append(C[len(C)-i-1])
                count += 1
            for i in range(count):
                C.pop()
            A.pop(0)
        else:
            C.append(A[0])
            A.pop(0)
            panduanA = False
        # print(A)
    else:
        if B[0] in C:
            count = 0
            B.append(B[0])
            for i in range(len(C)-C.index(B[0])):
                B.append(C[len(C)-i-1])
                count += 1
            for i in range(count):
                C.pop()
            B.pop(0)
        else:
            C.append(B[0])
            B.pop(0)
            panduanA = True
jieguo = ''
if len(A) == 0:
    for i in B:
        jieguo += i
else:
    for i in A:
        jieguo += i
print(jieguo)

