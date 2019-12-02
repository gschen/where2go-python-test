'''
3. 有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13 求出这个数列的前20项之和
提示：用递归

'''
def ccc(n):
    if n==1:
        return 1
    return n+(n+ccc(n-1))/n
print(ccc(20))