'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。`
'''
import numpy as np
l=[3,1,2,-2,-1,0]
l2=[]
for a in l:
    for b in l:
        for c in l:
            if a+b+c==0 and a>b>c:
                l2.append([a,b,c])
print(np.array(l2).reshape(len(l2),3))
