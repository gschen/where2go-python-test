'''
数学老师给小明出了一道等差数列求和的题目。但是粗心的小明忘记了一
部分的数列，只记得其中 N 个整数。
现在给出这 N 个整数，小明想知道包含这 N 个整数的最短的等差数列有
几项？
【输入格式】
输入的第一行包含一个整数 N。
第二行包含 N 个整数 A 1 ,A 2 ,··· ,A N 。(注意 A 1 ∼ A N 并不一定是按等差数
列中的顺序给出)
【输出格式】
输出一个整数表示答案。
【样例输入】
5
2 6 4 10 20
【样例输出】
10
【样例说明】
包含 2、6、4、10、20 的最短的等差数列是 2、4、6、8、10、12、14、16、
18、20。
'''
n = int(input())
lis = sorted(list(map(int, input().split())))
lis2 = []
for i in range(len(lis)-1):
    lis2.append(lis[i+1] - lis[i])
for j in range(2, min(lis2)+1):
    for p in lis2:
        if p % j != 0:
            break
    else:
        d = j
        break
else:
    d = 1
lis3 = list(x for x in range(min(lis), max(lis)+1, d))
print(len(lis3))
