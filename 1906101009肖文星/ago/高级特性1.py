def xwx(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return xwx(s[1:])
    elif s[-1:] == ' ':
        return xwx(s[:-1])
s=' a b '
print(xwx(s))
s='a b '
print(xwx(s))
s=' a b'
print(xwx(s))