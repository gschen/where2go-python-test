# 选择排序
# [10,9,13,5,25,70,2]

def select_sort(list):
    lenth = len(list)
    for i in range(0, lenth):
        max_num = i
        for o in range(i + 1, lenth):
            if list[i] > list[o]:
                max_num = o
                list[i], list[o] = list[o], list[i]
    return list


if __name__ == "__main__":
    print(select_sort([10, 100, 13, 5, 25, 70, 2]))

# 选择最大的或者最小的值插入到开头或者结尾
