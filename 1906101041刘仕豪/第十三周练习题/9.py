'''
18.字母连连看,给定一个由小写英文字母组成的字符串(长度 <1000),如果字符串中有两个连续的字母相同，则这两个字母可同时消除，并不断重复该操作，直到不能消除为止。请编程判断该字符串是否可以完全消除。
输入说明:一个字符串。
输出说明:如果可以完全消除，输出"YES" ,如果不可以,输出消除后的结果。
输入样例1: abacddcaba
输出样例1: YES
输入样例2: asdfghhgf
输出样例2: asd
'''
def xiaochu(s):
    l = []
    for i in s:
        l.append(i)
    for j in l:
        for k in l:
            if l.index(k) != l.index(j) and k == j:
                l.remove(k)
                l.remove(j)
            return l

