#有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和.提示：用递归
a=1
b=2
sum=0
for i in range(20):
    sum=a/b+sum
    a,b=(a+b),a
    print(sum)