# 2.星系炸弹
# 在X星系的广袤空间中漂浮着许多X星人造“炸弹”，用来作为宇宙中的路标。
# 每个炸弹都可以设定多少天之后爆炸。
# 比如：阿尔法炸弹2015年1月1日放置，定时为15天，则它在2015年1月16日爆炸。
# 有一个贝塔炸弹，2014年11月9日放置，定时为1000天，请你计算它爆炸的准确日期。
# 请填写该日期，格式为 yyyy-mm-dd 即4位年份2位月份2位日期。比如：2015-02-19
import datetime
strTime='2014-11-09'
startTime=datetime.datetime.strptime(strTime, '%Y-%m-%d')#将str转化位时间的表达式
startTime2=(startTime+datetime.timedelta(days=1000)).strftime("%Y-%m-%d")
print(startTime2)
