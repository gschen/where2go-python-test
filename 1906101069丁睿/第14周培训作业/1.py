def my_1(q):
    dr=[]
    for i in q:
        if i not in dr:
            dr.append(i)
    return len(dr),dr
print(my_1([1,1,2,2,3,4]))
