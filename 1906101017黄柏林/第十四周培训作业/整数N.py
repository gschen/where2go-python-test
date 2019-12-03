'''
给定一个正整数N，将其表示为数字1,2,5,11相加的形式输出。 要求上述数字出现的总次数最少(每个数字可以重复使用)。
'''

x = int((input()))
N = x
nums = [1,2,5,11]
list1 = []
for i in sorted(nums)[::-1]:
    while x >= i:
        list1.append(str(i))
        x -= i
print("%d="%N,end="")
print("+".join(list1))