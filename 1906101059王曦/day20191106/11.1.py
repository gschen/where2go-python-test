#每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。
#注意，除 N = 0 外，任何二进制表示中都不含前导零。
#二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。
#给定十进制数 N，返回其二进制表示的反码所对应的十进制整数
def erf(x):
    list2 = []
    list3 = []
    list1 = [a for a in bin(x)]
    list1.pop(0);list1.pop(0)
    list2 = [int(c) for c in list1 ]
    for b in list2:
        if b == 0:
            list3.append(str(1))
        else:
            list3.append(str(0))
    list3 = ''.join(list3)
    return int(list3,2)


print(erf(10))