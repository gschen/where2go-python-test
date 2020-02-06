A = []
B = []
C = []

for i in open("E:\测试A.txt",encoding='UTF-8'):
    A.append(i[:-1])
for i in open("E:\测试B.txt",encoding='UTF-8'):
    B.append(i[:-1])
for i in open("E:\测试C.txt",encoding='UTF-8'):
    C.append(i[:-1])

count = 0
for i in A:
    for j in B:
        if i in C:
            continue
        if i==j:
            count+=1
print(count)

'''
文本 测试A 中内容为：
黄一
王二
张三
李四
麻子
文本 测试B 中内容为：
王二
张三
黄一
麻子
文本 测试C 中内容为：
王二
李四
麻子
'''