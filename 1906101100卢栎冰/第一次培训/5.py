count = 0
for i in range(1,100001):
    a = str(i)
    if str(i) == str(i)[::-1]:
        count += 1
        print(i)
print(count)



