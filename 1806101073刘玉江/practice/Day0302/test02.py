num = 12321
def isPalindrome(num):
    s_num = str(num)
    ls=[]
    for i in s_num:
        ls.append(i)
    strx = ""
    for i in range(len(ls)):
        strx = strx + ls.pop()
    return strx == s_num


def isPalindrome1(x):
    str_x = str(x)
    for i in range(len(str_x)//2):
        if str_x[i] != str_x[len(str_x)-1-i]:
            return False
    return True

    
print(isPalindrome1(num))