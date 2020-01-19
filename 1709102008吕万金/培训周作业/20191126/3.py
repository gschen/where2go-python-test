'''
3. 有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
提示：用递归

'''
def ccc(n,a,b,sum):
    sum+=(a+b)/a
    if n<19:
        return ccc(n+1,a+b,a,sum)
    if n==19:
        return sum
print(ccc(1,2,1,2))

# n=int(input())
# a=2
# b=1
# sum=0
# for i in range(n):
#     c = a / b
#     sum+=c
#     a,b=a+b,a
# print(sum)