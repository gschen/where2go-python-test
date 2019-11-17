"""
输出杨辉三角
"""
def triangles(x):
    a = [1]
    for i in range(x):
        print(a)
        a = [1] +[x+a[i+1] for i,x in enumerate(a[:-1])] + [1]

    return ""
v= int(input())
print(triangles(v))