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