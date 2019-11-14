"""
切面条
"""
def qie(x):
    if x == 0:
        return 2
    else:
        return qie(x-1)*2-1
n = int(input())
print(qie(n))