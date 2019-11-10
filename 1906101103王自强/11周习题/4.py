'''4.	请使用“栈”的方法完成括号匹配（给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。）'''
def isValid(s):
    box=[]
    right=['(','[','{']
    left=[')',']','}']
    s_1=list(s)
    for i in s_1:
        if i in right or i in left:
            box.append(i)
    l=[]
    for j in box:
        if m in right:
            l.append(m)
        elif m==')'and l[-1]=='(':
            l.pop(m)
        elif m==']'and l[-1]=='[':
            l.pop(m)
        elif m=='}'and l[-1]=='{':
            l.pop(m)
    if len(l)==0:
        return True
    else:
        return False