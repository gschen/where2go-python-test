#3. 有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
#提示：用递归
n=int(input("输入项数："))
a=2
b=1
sum=0
for i in range(n):
    sum = sum + (a / b)
    a,b = a+b,a
print(sum)