'''
白狼杰洛特所居住的猎魔人城堡遭到狂猎入侵，杰洛特无法集中全部的精力迎敌，只得只能顾得首尾两地，中间大军则无力管教，只能放纵送杀，
给定一个数字，其在二进制状态下的保留首1和尾1，其余中间部分全部舍去(如果是负数则按照正数处理)。
如13的二进制为： 0000 1101 其舍弃中间部分就变成了 0000 1001 结果为 9
'''
# print(bin(54)[2:])
def erjinzhi(n):
    s = '1'
    e = bin(n)[2:]
    k = len(e)
    while e[k-1] == '0':
        k -= 1
    for i in range(1,k-1):
        s = s + '0'
    s = s + '1'
    return s


def sha():
    m = int(input())
    l = []
    while m > 0:
        a = int(input())
        m -= 1
        l.append(a)
    for j in l:
        j = erjinzhi(j)
        j = eval('0b' + j)
        print(j)
sha()