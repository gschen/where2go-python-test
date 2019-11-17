'''7、	给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度'''
zifu=input()
l=list(zifu)
box=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j] and i<j:
            l_2=set(l[i:j])
            box.append(len(l_2))
if box!=[]:
    x=max(box)
else:
    x=len(l)
print(x)