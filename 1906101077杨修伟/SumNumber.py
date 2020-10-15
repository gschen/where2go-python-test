n = int(input())
s =0
for i in range(1,n+1):
    for j in str(i):
        if j == "2" or j == "0" or j == "1" or j == "9":
            s += int(i)
            break
print(s)
