N,M = input().split()
num = sorted(input().split())

add = 0
delete = 0

for i in range(int(M)):
    delete -= int(num[i])
    # print(delete)
for j in range(len(num)-int(M)):
    add += int(num[len(num)-j-1])

print(add+delete)