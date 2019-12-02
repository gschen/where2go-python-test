#给定一个数组，你需要删除重复出现的元素，使得每个人元素只出现一次，返回移除后数组的新长度和新的数组
ls=[1,1,1,2,3,4,4,4]
for x in range(len(ls)-1):
    for y in ls[x+1: ]:
        if ls[x] == y:
            ls.remove(ls[x])
        else:
            break
print(len(ls))
print(ls)
