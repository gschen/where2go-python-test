'''10、给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
'''
def isValid(s):
    box=[]
    right=['(','[','{']
    left=[')',']','}']
    s_1=list(s)
    for i in s_1:
        if i in right or i in left:
            box.append(i)