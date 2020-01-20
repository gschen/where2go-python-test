n = int(input())
list1 = list(map(int,input().split()))
print(list1)
s = 0
for i in list1:
    if (list1.index(i))+1!=i :
        list1[list1.index(i)]=list1[i-1]
        list1[i-1]=i
        print(list1)
        s += 1
print(s)
