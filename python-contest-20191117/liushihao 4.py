a = input()
n = int(input())

suzhu = []

def kmp_match(s, p):
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)
                break
        else:
            return True
    return False


# 部分匹配表
def partial_table(p):
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret

for i in range(n):
    a = input()
    suzhu.append(a)

for i in range(len(suzhu)):
    print(kmp_match(a,suzhu[i]))
