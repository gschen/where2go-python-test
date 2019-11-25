x=input("请输入第一个数字:")
y=input("请输入第二个数字:")
z=input("请输入第三个数字:")
arr=[x,y,z]
for i in range(0,3):
    for j in range(i,3):
        if int(arr[i])>int(arr[j]):
            k=arr[i]
            arr[i]=arr[j]
            arr[j]=k
print(arr)

