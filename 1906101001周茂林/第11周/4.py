'''
请使用“栈”的方法完成括号匹配
（给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。）
()[{]}
'''
def zhan(s):
    l = []
    for i in s:
        if i == '(' or i == '[' or i == '{': l.append(i)
        elif i == ')' and l[-1] == '(': l.pop()
        elif i == ']' and l[-1] == '[': l.pop()
        elif i == '}' and l[-1] == '{': l.pop()
    return len(l) == 0




s = "(([){}])"
result = zhan(s)
print(result)
