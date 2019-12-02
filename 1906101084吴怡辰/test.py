L={'Jack':[90,80,60],'Machile':[80,60,30],'Bob':[80,70,90]}
#定义一个求总成绩的函数
def sum(ls):
    sum=0
    for i in ls:
        sum+=i
    return sum
#遍历列表中的键
for i in L:
    print(i,end=" 总成绩：")
    x=map(sum,[L[i]])
    for j in x:
        print(j,end=" 平均成绩：")
        print(j/3)