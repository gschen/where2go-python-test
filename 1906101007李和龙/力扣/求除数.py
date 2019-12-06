"""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。
示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
"""

def get_quotient(dividend,divisor):
    quotient = 0
    if dividend > 0 and divisor > 0:
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
    elif dividend < 0 and divisor < 0:
        while dividend <= divisor:
            dividend -= divisor
            quotient += 1
    else:
        _end = abs(dividend)
        _sor = abs(divisor)
        while _end >= _sor:
            _end -= _sor
            quotient -= 1
    return quotient

if __name__ == "__main__":
    dividend,divisor = map(int,input().split())
    print(get_quotient(dividend,divisor))