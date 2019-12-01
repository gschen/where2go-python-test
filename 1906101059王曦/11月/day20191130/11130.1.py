#生成杨辉三角
def triangles():
    list1 = [1]
    while True:
        yield list1
        list1.append(0)
        list1 =[list1[i]+list1[i-1] for i in range(len(list1))]



n = 0
for s in triangles():
    print(s)
    n +=1
    if n == 10:
        break