'''
4. 给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。
要求上述数字出现的总次数最少(每个数字可以重复使用)。
输入说明:一个正整数N (N<= 10000)。

输入：21
输出：11
	   5
	   5
'''
num=int(input())
l1=[11,5,2,1]
l2=[]
for i in l1:
    while num>=i:
        num-=i
        l2.append(i)
for ccc in l2:
    print(ccc)