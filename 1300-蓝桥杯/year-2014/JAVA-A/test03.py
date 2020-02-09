'''
3.标题：神奇算式
'''
import collections
def is_repeat(strs):
    dic=collections.Counter(strs)
    for i in dic.values():
        if i>1:
            return True
    return False
def is_part(result,strs):
    for i in strs:
        if i not in result:
            return False
    return True

for i in range(1001):
    for j in range(1001):
        if i*j>=10000:
            pass
        else:
            strs=str(i)+str(j)
            if not is_repeat(strs) and is_part(str(i*j),strs) and 1000<i*j:
                print(str(i)+"x"+str(j)+"="+str(i*j))
