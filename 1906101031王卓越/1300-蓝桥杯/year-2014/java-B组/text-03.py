# 3.标题：猜字母

#     把abcd...s共19个字母组成的序列重复拼接106次，得到长度为2014的串。

#     接下来删除第1个字母（即开头的字母a），以及第3个，第5个等所有奇数位置的字母。

#     得到的新串再进行删除奇数位置字母的动作。如此下去，最后只剩下一个字母，请写出该字母。

# 答案是一个小写字母，请通过浏览器提交答案。不要填写任何多余的内容。
li=[chr(x) for x in range(97,116)]
for num in range(106):
    for i in range(97,116):
        li.append(chr(i))
lis=[]
while len(lis)!=1:
    num2=len(lis)-1
    for n in range(0,num2):
        if n%2==0:
            lis.append(li[n])
        if n==num2:
            for x in lis:
                li.remove(x)
print(li[0])



