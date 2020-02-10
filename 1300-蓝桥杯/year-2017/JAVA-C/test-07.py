begin = input()
end = input()
a = []
A = set(a)
A.add(begin)

def sub(string, p, c):   #定义 * 的变动
    new = []
    for s in string:
        new.append(s)
    a = new[p]
    new[p] = new[c]
    new[c] = a
    A.add(''.join(new))

count = 0
while end not in A:
    for i in list(A):
        index = i.index('*')
        if len(i)-index-1>= 3:
            sub(i, index, index + 1)
            sub(i, index, index + 2)
            sub(i, index, index + 3)
        if index>=3:
            sub(i, index, index - 1)
            sub(i, index, index - 2)
            sub(i, index, index - 3)
        if len(i)-index-1 < 3:
            for j in range(len(i) - index - 1):
                sub(i, index, index+j+1)
        if index < 3:
            for j in range(index):
                sub(i, index, index+j+1)
    count += 1
print(count)

