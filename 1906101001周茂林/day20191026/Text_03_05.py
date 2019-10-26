a = input()
list1 = []
for i in a:
    if i.isdigit():
        list1.append(i)
print(''.join(list1))