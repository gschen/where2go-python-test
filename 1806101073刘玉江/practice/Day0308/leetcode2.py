def numTimesAllBlue(light):
    ls=[]
    for i in range(len(light)):
        ls.append(0)
    x = 0
    ls1=[]
    for i in light:
        ls1.append(i)
        ls[i-1]=1
        ans = 1
        for j in ls[0:max(ls1)-1]:
            ans = ans * j
        if ans != 0:
            for z in range(len(ls[0:i-1])):
                ls[z] = 2
            x = x +1
    return x

import numpy as np
def numTimesAllBlue1(light):
    ls=np.zeros(len(light))
    x = 0
    num=0
    for i in light:
        if i > num:
            num = i
        ls[i-1]=1
        if 0 not in ls[0:num-1]:
            x = x + 1
    return x
print(numTimesAllBlue1([1,2,3,4,5,6]))


