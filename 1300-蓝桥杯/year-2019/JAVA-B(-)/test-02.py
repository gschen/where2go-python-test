a = '0100110001010001'
A = set()
for i in range(len(a)):
    for j in range(i,len(a)):
        A.add(a[i:j+1])
print(len(A))