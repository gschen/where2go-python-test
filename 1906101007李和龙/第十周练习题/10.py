"""
10、给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。

"""
string = input("请输入一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串：")
lenth = int(len(string))
if lenth % 2 == 1:
    print("false,只有奇数个字符")
if lenth % 2 == 0:
    for n in range(int(lenth)):
        for m in range(len(string) - 2):
            a = string[m] == "(" and string[m+1] == ")"
            b = string[m] == "[" and string[m+1] == "]"
            c = string[m] == "{" and string[m+1] == "}"
            if a or b or c:
                string = string[:m] + string[m+2:]
                break
    if len(string) > 2:
        print("false")
    if len(string) == 2:
        d = ["()","{}","[]"]
        if string in  d:
            print("true")
        else:
            print("false")
