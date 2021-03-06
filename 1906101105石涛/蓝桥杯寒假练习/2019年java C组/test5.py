# coding=utf-8

'''
试题 E: 最大降雨量
本题总分：15 分
【问题描述】
由于沙之国长年干旱，法师小明准备施展自己的一个神秘法术来求雨。 这个法术需要用到他手中的 49 张法术符，
上面分别写着 1 至 49 这 49 个 数字。法术一共持续 7 周，每天小明都要使用一张法术符，法术符不能重复使 用。
每周，小明施展法术产生的能量为这周 7 张法术符上数字的中位数。法术 施展完 7 周后，求雨将获得成功，降雨量为 7 周能量的中位数。
 由于干旱太久，小明希望这次求雨的降雨量尽可能大，请大最大值是多少？
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一 个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
'''
# (思路：总共七组，每组七个数字，想要中值最大，就得中值最大的三组中最大的4个值大于这个值，还有它自己的最大的三个值，把他们都当作最大的值，反过来减去就可以了)
print(49-3*4-3)