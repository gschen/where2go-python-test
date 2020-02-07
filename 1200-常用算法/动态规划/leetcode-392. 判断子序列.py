

def f(s,t):
    m = len(s)
    n = len(t)
    
    a = [[0 for i in range(n+1)] for j in range(m+1)]

    for j in range(0, n+1):
        a[0][j] = True
    for i in range(1, m+1):
        a[i][0] = False
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i > j:
                a[i][j] = False
                continue
            
            if i == 1:
                a[i][j] = a[i][j-1] or s[i-1] == t[j-1]
                continue
            
            if (a[i-1][j-1] == True and s[i-1] == t[j-1]) or a[i][j-1] == True:
                a[i][j] = True
            else:
                a[i][j] = False

    return a[-1][-1]

print(f('axc', 'ahbgdc'))