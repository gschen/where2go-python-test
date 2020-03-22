def countCharacters(words,chars):
    res = 0
    for i in range(len(words)):
        n = 0
        lsc=[i for i in chars]
        for j in range(len(words[i])):
            if words[i][j] not in lsc:
                break
            n += 1
            lsc.remove(words[i][j])
        if len(words[i]) == n:
            res += n
    return res


def countCharacters1(words,chars):
    res=0
    for i in words:
        for j in i:
            if i.count(j) <= chars.count(j):
                flag = 1
                continue
            else:
                flag = 0
                break
        if flag == 1:
            res += len(i)
    return res



print(countCharacters1(["cat","bt","hat","tree"],
                      "atach"))