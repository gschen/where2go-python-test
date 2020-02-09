'''
2.标题：切面条
'''
def cut_m(n):
    if n==0:
        return 2
    else:
        return cut_m(n-1)*2-1
print(cut_m(10))
