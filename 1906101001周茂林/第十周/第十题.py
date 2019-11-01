'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
'''
# '[]{}()'   '[{()}]'  当类似两种情况都不符合时，FFFF
def qqaa(s):
    if len(s) % 2 != 0:
        print('TTTT')
    else:
        m = 0
        while m < len(s)-2:
            if s[m] == '(' and s[m+1] == ')' or s[m] == '[' and s[m+1] == ']' or s[m] == '{' and s[m+1] == '}':
                m += 2
                continue
            else:
                while m < len(s)/2:
                    if s[m] == '(' and s[-m-1] == ')' or s[m] == '[' and s[-m-1] == ']' or s[m] == '{' and s[-m-1] == '}':
                        m += 1
                        continue
                    else:
                        print('FFFF')
                        m = -1
                        break
                break
        if m != -1:
            print('TTTT')


qqaa('([{}])')