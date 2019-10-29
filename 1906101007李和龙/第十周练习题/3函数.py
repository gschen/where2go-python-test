"""
3、	编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
def hanshu(a):
    if a %2 == 0:
        if a == 2:
            return 1/2
        else:
            return 1/a + hanshu(a-2)
    else:
        if a == 1:
            return 1
        else:
            return 1/a + hanshu (a-2)
m = int(input())
print(hanshu(m))
