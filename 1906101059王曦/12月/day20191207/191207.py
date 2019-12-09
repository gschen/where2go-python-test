#判断句子中单词的长度
s = str(input())
l = []
l2 = []
for i in range(len(s)):
    if s[i]==' ':
        l.append(i)
l.append(len(s))
for i in range(len(l)):
    if i<len(l)-1:
        d = l[i+1]-l[i]-1
        l2.append(d)
l2.insert(0,l[0])
print(l2)