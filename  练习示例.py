import unittest

def sum(a, b):
    '''两个整数求和
    Params:
    a - 第一个整数
    b - 第二个整数

    Return:
    a和b之和。
    '''
    return a + b

class SumTest(unittest.TestCase):

    # 第一个测试用例
    def test_01(self):
        self.assertEqual(sum(2,3), 5)

    def test_02(self):
        self.assertEqual(sum(-10,10), 0)

    def test_03(self):
        self.assertEqual(sum(1,2), 4)

if __name__ == '__main__':
    unittest.main()