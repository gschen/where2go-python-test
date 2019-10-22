'''
1、	有四个字母：a、b、c、d，能组成多少个互不相同且无重复三位字符串？输出所有结果。
'''
A = ['a','b','c','d']
print("共有24种结果，分别为：")
for x in range(0,4):
    for y in range(0,4):
        for z in range(0,4):
            if x!=y and y!=z and x!=z:
                print("{}{}{}".format(A[x],A[y],A[z]))