from datetime import datetime
sr = datetime(1999,9,2)
print(sr.isoformat())
print(sr.year,'年',sr.month,'月',sr.day,'日')
print(sr.day,'日',sr.month,'月',sr.year,'年')
print(sr.strftime('%Y-%m-%d'))
print(sr.strftime('%d-%m-%Y'))
print(sr.strftime('%Y~%m~%d'))
print(sr.strftime('%Y.%m.%d'))
print(sr.strftime('%Y:%m:%d'))
print('{0:%Y}年{0:%m}月{0:%d}日'.format(sr))
print('{0:%d}日{0:%m}月{0:%Y}年'.format(sr))
