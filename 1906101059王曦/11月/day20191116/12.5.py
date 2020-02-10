# 白狼杰洛特所居住的猎魔人城堡遭到狂猎入侵
# 杰洛特无法集中全部的精力迎敌，只得只能顾得首尾两地，中间大军则无力管教，只能放纵送杀，
# 给定一个数字，其在二进制状态下的保留首1和尾1，
# 其余中间部分全部舍去(如果是负数则按照正数处理)。
# 如13的二进制为： 0000 1101 其舍弃中间部分就变成了 0000 1001 结果为 9
k = int(input())
s = 0
list3 = []
while k>0:
    x = int(input())
    x = abs(x)
    list1 = list(bin(x))
    k-=1
    list1.pop(0)
    list1.pop(0)
    s = list1.index('1')
    n = list1[::-1].index('1')
    b = list1[1:len(list1)-n-1]
    if b == []:
        list2 = [int(i)for i in list1[s:len(list1)]]
    else:
        list2 = [1]+[int(i)*0 for i in b]+[int(i) for i in list1[len(list1)-n-1:len(list1)]]
    c = len(list2)
    for i in list2:
        s = s+i*2**(c-1)
        c-=1
    list3.append(s)
for m in list3:
    print(m)