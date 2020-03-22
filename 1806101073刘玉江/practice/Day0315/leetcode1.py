def luckyNumbers(matrix):
    mindic={}
    res=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == min(matrix[i]):
                mindic[matrix[i][j]] = j
    for i in mindic:
        maxls = []
        for j in range(len(matrix)):
            maxls.append(matrix[j][mindic[i]])
        if i == max(maxls):
            res.append(i)
    return res


print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))