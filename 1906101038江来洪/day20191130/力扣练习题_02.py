"""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def jiang(dividend,divisor):
    num = 0
    if dividend >= 0 and divisor >= 0:
        while dividend >= divisor:
            num += 1
            dividend -= abs(divisor)
        return num
    else:
        dividend,divisor = abs(dividend),abs(divisor)
        while dividend >= divisor:
            num -= 1
            dividend -= abs(divisor)
        return num
print(jiang(7,-3))