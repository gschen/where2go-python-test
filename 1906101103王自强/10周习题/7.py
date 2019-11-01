'''7、	给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。'''
'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_str=len(s)
        #存储所有非重复子序列的长度
        final_len=[]
        #对序列进行遍历，未重复时进行字符串的拼接，重复时跳出拼接，进行下一轮的遍历
        for i in range(len_str):
            data1=s[i]
            for j in range(i+1,len_str):
                if s[j] not in data1:
                    data1=data1+s[j]      
                else:
                    break
            final_len.append(len(data1))
        #判断当存储的非重复子序列为空时，s是为空格,为空格字符时，非重复字符长度为1，为空字符时，非重复的字符长度为0
        if final_len==[]:
            if s=='':
                final_len.append(0)
            else:
                final_len.append(1)
        return(max(final_len))'''