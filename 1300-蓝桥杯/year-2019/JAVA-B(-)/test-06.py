a = int(input())

count = 0
for i in range(1,a+1):
    if '2' in list(str(i)):
        count += i
    elif '0' in list(str(i)):
        count += i
    elif '1' in list(str(i)):
        count += i
    elif '9' in list(str(i)):
        count += i
print(count)