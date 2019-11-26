'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
'''

def kuohaopipei(s):
    l = []
    kuohao="()[]{}"
    for i in range(len(s)):
        si = s[i]
        if kuohao.find(si) == -1:
            continue
        if si == '(' or si == '[' or si == '{':
            l.append(si)
            continue
        if len(l) == 0:
            return False
        p = l.pop()
        if ( p == '(' and si == ')') or(p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False
    if len(l) > 0:
        return False
    return True
