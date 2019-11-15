'''
白狼杰洛特所居住的猎魔人城堡遭到狂猎入侵，杰洛特无法集中全部的精力迎敌，只得只能顾得首尾两地，中间大军则无力管教，只能放纵送杀，给定一个数字，其在二进制状态下的保留首1和尾1，其余中间部分全部舍去(如果是负数则按照正数处理)。
如13的二进制为： 0000 1101 其舍弃中间部分就变成了 0000 1001 结果为 9
'''
n = int(input())
lis = list(x for x in range(n))
for i in range(n):
    lis[i] = int(input())
for j in lis:
    s = bin(j)
    s = list(s)
    for i in s:
        if i == '-' or i == 'o' or i == 'b':
            s.remove(i)
    q = s.index('1')
    p = len(s) - s[::-1].index('1') -1
    for m in range(len(s)):
        if m > q and m < p:
            s[m] = '0'
    s = "".join(s)
    print(int(s,2))