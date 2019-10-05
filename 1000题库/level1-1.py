import unittest

# 定义函数，以函数的形式来解决问题。
# 问题URL: 
def fn_sum(n):
    ''' 1-n求和 #问题描述
    Params:
    n - 自然数n

    Return:
    1-n的和.
    '''
    # 实现此处代码。
    return 0


class Test(unittest.TestCase):
    # 通过全部的测试用例表示问题解决。
    # 第一个测试用力
    def test_01(self):
        self.assertEqual(fn_sum(100), 5050)

    def test_02(self):
        self.assertEqual(fn_sum(3), 6)


if __name__ == '__main__':
    unittest.main()

