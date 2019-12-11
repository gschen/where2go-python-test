def palindromePartition(s,k):
    n = len(s)
    if n%k != 0:
        a = int(n/k)+1
    elif n%k == 0:
        a =n/k
    num=0
    for i in range(n):
        if i+a < n-1:
            s1 = s[i:i+a]
        else:
            s1 = s[i:-1]
        for j in range(len(s1)-1):
            if s1[j] == s1[j+1]:
                num=0
            else:
                num = num + 1
    return  num
