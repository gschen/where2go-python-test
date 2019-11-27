#插入排序
#[10,9,13,5,25,70,2]

def insert_sort(list):
    lenth = len(list)
    for i in range(1,lenth):
        j = i
        while j >= 1:
            if list[j] > list[j-1]:     #从大到小，从小到大只需要改这里的>符号
                list[j],list[j-1] = list[j-1],list[j]
                j -= 1
            else:
                break
    return list
    return "END"
if __name__ == "__main__":
    print(insert_sort([10,9,13,5,25,70,2]))