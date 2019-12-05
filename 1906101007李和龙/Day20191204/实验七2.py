"""
4.求和 求s= a + aa + aaa + … + aa…a 的值（最后一个数中 a 的个数为 n ），
   其中 a 是一个1~9的数字，例如： 2 + 22 + 222 + 2222 + 22222 （此时 a=2 n=5 ）
输入：一行，包括两个整数，第1个为a，第2个为n（1 ≤ a ≤ 9，1 ≤ n ≤ 9），
      以英文逗号分隔。
输出：一行，s的值。
输入例子：2,5 对应输出：24690

"""


def get_sum(a, n):
    a = str(a)
    list_nums = []
    sum = 0
    for i in range(n):
        list_nums.append(a)
        num = "".join(list_nums)
        sum += int(num)
    return sum


a, n = map(int, input().split(","))
print(get_sum(a, n))
