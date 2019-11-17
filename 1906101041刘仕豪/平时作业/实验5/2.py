'''
2.请写一个函数，实现删除字符串当中的首尾空格，请用切片操作，不要使用strip()函数
'''
def del_kong(s):
    def a(s):
        i = 0
        k = len(s)
        if k == 0:
            return s
        while i < k and s[i] == ' ':
            i += 1
            if i == k:
                return s[i:]
        while s[k - 1] == ' ':
            k -= 1
        s = s[i:k]
        return s
