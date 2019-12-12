"""
标题：书号验证

2004年起，国际ISBN中心出版了《13位国际标准书号指南》。
原有10位书号前加978作为商品分类标识；校验规则也改变。
校验位的加权算法与10位ISBN的算法不同，具体算法是：
用1分别乘ISBN的前12位中的奇数位（从左边开始数起），用3乘以偶数位，乘积之和以10为模，10与模值的差值再对10取模（即取个位的数字）即可得到校验位的值，其值范围应该为0~9。

输入：9 7 8-7-3 0 1-0 4 8 1 5-3     	9 8 3  1 4 1
				21  21 24 15      1

输出：true
解释：该ISBN的第13位校验和是3，结果计算正确，返回true。

输入：978-7-115-38821-5			9 8 1 5 8 2             3
					21 21 3 9 24 3········1
输出：false
解释：该ISBN的第13位校验和是6，结果计算错误，返回false。

"""
def book_code(code):
    code_list = []
    new_list = []
    for i in code:
        if 48<=ord(i)<=57:
            code_list.append(i)
    jishu = int(code_list[0]) +int(code_list[2])+int(code_list[4])+int(code_list[6])+int(code_list[8])+int(code_list[10])
    oushu = 3*(int(code_list[1]) +int(code_list[3])+int(code_list[5])+int(code_list[7])+int(code_list[9])+int(code_list[11]))
    sums = jishu + oushu
    new_sum = 10 -(int(sums) % 10)
    if new_sum == int(code_list[12]):
        return "ture"
    else:
        return "false"
print(book_code("978-7-115-38821-5"))