L=input()
S=input()

trans_str={'A':'T','T':'A','G':'C','C':'G'}
#将目标串翻译
def trans(trans_str,S):
    retrun_str = ''
    for i in range(len(S)):
            retrun_str=retrun_str+trans_str[S[i]]
    return retrun_str

#目标串翻译后
#计算回溯表

def prefix_nums(patten_str):
    return_prfix_nums=[0]
    i_index=0
    j_index=1
    while j_index<len(patten_str):
        if patten_str[i_index]==patten_str[j_index]:
            return_prfix_nums.append(return_prfix_nums[-1]+1)
            i_index+=1
            j_index+=1
        else:
            return_prfix_nums.append(0)
            i_index=0
            j_index+=1
    #进行后移一位
    for  k_index in range(len(return_prfix_nums)-1,0,-1):
        return_prfix_nums[k_index]=return_prfix_nums[k_index-1]
    return_prfix_nums[0]=-1
    return return_prfix_nums

#kmp算法 计算匹配成功的第一个下标
def kmp(AIM_str,patten_str):
    i_index=0
    j_index=0
    next_nums=prefix_nums(patten_str)
    while i_index<len(AIM_str) and j_index<len(patten_str):
        if AIM_str[i_index]==patten_str[j_index]:
            i_index+=1
            j_index+=1
        else:
            if next_nums[j_index]==-1:
                j_index = 0
                i_index+=1

            else:
                j_index=next_nums[j_index]
    print(i_index-j_index+1)

trans_S=trans(trans_str,S)
print(prefix_nums(trans_S))
kmp(L,trans_S)




