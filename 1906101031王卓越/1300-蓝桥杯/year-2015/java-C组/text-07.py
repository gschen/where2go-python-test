# 第七题：打印大X
# 题目描述
# 小明希望用星号拼凑，打印出一个大X，他要求能够控制笔画的宽度和整个字的高度。
# 为了便于比对空格，所有的空白位置都以句点符来代替。

# 要求输入两个整数m n，表示笔的宽度，X的高度。用空格分开(0<m<n, 3<n<1000, 保证n是奇数)
# 要求输出一个大X

# 例如，用户输入：
# 3 7
# 程序应该输出：
# ***.....***
# .***...***.
# ..***.***..
# ...*****...
# ....***....
# ...*****...
# ..***.***..
# .***...***.
# ***.....***

# （如有对齐问题，参看【图1.jpg】）

# 再例如，用户输入：
# 4 21
# 程序应该输出
# ****................****
# .****..............****.
# ..****............****..
# ...****..........****...
# ....****........****....
# .....****......****.....
# ......****....****......
# .......****..****.......
# ........********........
# .........******.........
# ..........****..........
# .........******.........
# ........********........
# .......****..****.......
# ......****....****......
# .....****......****.....
# ....****........****....
# ...****..........****...
# ..****............****..
# .****..............****.
# ****................****

# （如有对齐问题，参看【图2.jpg】）


# 资源约定：
# 峰值内存消耗（含虚拟机） < 256M
# CPU消耗  < 1000ms


# 请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

# 所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
# 注意：不要使用package语句。不要使用jdk1.7及以上版本的特性。
# 注意：主类的名字必须是：Main，否则按无效代码处理。
a,b=map(int,input().split(' '))

    