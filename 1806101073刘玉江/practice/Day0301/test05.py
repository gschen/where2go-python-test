# 动态规划

import numpy as np

arr = [1, 2, 4, 1, 7, 8, 3]

# 递归
def rec_opt(arr,i):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])
    if i >= 2:
        return max(rec_opt(arr,i - 2) + arr[i], rec_opt(arr,i - 1))

# 非递归
def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2]+arr[i]
        B = opt[i-1]
        opt[i]=max(A,B)
    return int(opt[-1])



def dp_opt2(arr):
    opt=[]
    opt.append(arr[0])
    opt.append(max(arr[0],arr[1]))
    for i in range(2,len(arr)):
        opt.append(max(opt[i-2]+arr[i],opt[i-1]))
    return int(opt[-1])

#print(rec_opt(arr,6))
#print(dp_opt(arr))
#print(dp_opt2(arr))


def subset(arr,i,s):
    if arr[i] == s:
        return True
    elif i == 0:
        return arr[0]==s
    elif arr[i]>s:
        return subset(arr,i-1,s)
    return subset(arr,i-1,s-arr[i]) or subset(arr,i-1,s)
#print(subset(arr1,5,s))
arr1=[1,5,3,2,6]
s=4

def dp_subset(arr,s):
    lis=np.zeros((len(arr),s+1),dtype=bool)

    lis[0,:] = False
    lis[:, 0] = True
    lis[0,arr[0]]=True
    for i in range(len(arr)):
        for j in range(s+1):
            if arr[i]>j:
                lis[i][j] = lis[i-1][j]
            else:
                lis[i][j] = lis[i-1][j] or lis[i-1][j-arr[i]]


    return lis[-1][-1]
print(dp_subset(arr1,s))