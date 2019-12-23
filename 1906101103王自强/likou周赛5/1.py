'''给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
示例 1：
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字 位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字
示例 2：
输入：nums = [555,901,482,1771]
输出：1
解释：
只有 1771 是位数为偶数的数字。
提示：
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
'''
import unittest
def fun(nums):
    sum=0
    for i in nums:
        if len(str(i))%2==0:
            sum+=1
    return sum
class funTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(fun(nums = [12,345,2,6,7896]), 2)
    def test_02(self):
        self.assertEqual(fun(nums = [555,901,482,1771]),1)
    def test_03(self):
        self.assertEqual(fun(nums=[125,9998,457,9995]),2)
if __name__ == '__main__':
    unittest.main()