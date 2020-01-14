'''立方变自身
观察下面的现象,某个数字的立方，按位累加仍然等于自身。
1^3 = 1 
8^3  = 512    5+1+2=8
17^3 = 4913   4+9+1+3=17
...
请你计算包括1,8,17在内，符合这个性质的正整数一共有多少个？
请填写该数字，不要填写任何多余的内容或说明性的文字
'''
sum=0
for i in range(1,100000):
    s=str(i**3)
    sum1=0
    for j in s:
        sum1+=int(j)
    if i==sum1:
        sum+=1
print(sum)