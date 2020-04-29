def feasible_index(box, nextx):  # box是一个存放每一行皇后位置的横坐标(即每个皇后所在列)，nestx表示下个皇后的横坐标
    if len(box)>0:
        if nextx in box:#第一种情况，下一个皇后的位置位于其他皇后位置的同一列
            return False
        elif nextx==box[-1]-1:#第二种情况，下一个皇后的位置位于上一个皇后的左对角线
            return False
        elif nextx==box[-1]+1:#第三种情况，下一个皇后的位置位于上一个皇后的右对角线
            return False
    return True  # 满足位置条件，返回True
def queen(feasible_box, n, ans):
    if len(feasible_box) == n:  # 当n个皇后都找到位置后，递归结束
        ans.append(feasible_box)  # 将可行棋盘加到ans列表中
    else:
        for i in range(n):  # 皇后没排完，开始在下一行加入皇后
            if feasible_index(feasible_box, i):  # 判断i位置是否可行
                queen(feasible_box + [i], n, ans) # 将可行的i位置加入棋盘feasible_box，然后递归
lis = []
queen([], 4, lis)
if len(lis)<2:
    print(0)
else:
    print(len(lis)*(len(lis)-1))
