def gcdOfStrings(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    def gcd(a, b):
        while a != 0:
            a, b = b % a, a
        return b
    maxx=gcd(len_str1,len_str2)
    if str1 + str2 != str2 + str1:
        return ""
    return str1[0:maxx]


print(gcdOfStrings('AAAA', 'AAAAAA'))
