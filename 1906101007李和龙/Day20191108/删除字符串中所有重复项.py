"""
1.	从Python中的给定字符串中删除所有重复项
"""
def hanshu (x):
    a = " ".join(set(x))
    return a

str = input("请输入一串字符：")
# aa = list()
# for i in str:
#     aa.append(i.split())
print(hanshu(str))