from functools import reduce
def raw(x,y):
    return x+y
mat=eval(input())
threshold=input()
for a in range(1,len(mat[0])):
    if reduce(raw,mat[a][:a])+reduce(raw,)



