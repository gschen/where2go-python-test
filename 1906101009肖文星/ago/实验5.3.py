from datetime import datetime
xwx = datetime(2001,2,27)
print(xwx.isoformat())
print('{0:%Y}年{0:%m}月{0:%d}日'.format(xwx))
print('{0:%d}日{0:%m}月{0:%Y}年'.format(xwx))
print(xwx.year,'年',xwx.month,'月',xwx.day,'日')
print(xwx.day,'日',xwx.month,'月',xwx.year,'年')
print(xwx.strftime('%Y-%m-%d'))
print(xwx.strftime('%d-%m-%Y'))
print(xwx.strftime('%Y=%m=%d'))
print(xwx.strftime('%Y/%m/%d'))
print(xwx.strftime('%Y:%m:%d'))


