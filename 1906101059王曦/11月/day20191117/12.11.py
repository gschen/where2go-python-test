#括号匹配
def kuo(s):
    l = []
    kuoh="()[]{}"
    for i in range(len(s)):
        si = s[i]
        if kuoh.find(si) == -1:
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