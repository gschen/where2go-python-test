"""
总词汇数统计和每个词汇的使用次数统
计。可以将每个词汇作为key保存到字典中，对文本从开始到结束，循
环处理每个词汇，并将词汇设置为一个字典的key，并将其value设置为
1，如果已经存在该词汇的key，说明该词汇已经使用过，就将value累加1。
"""

def wordcount(readtxt):
    readlist = readtxt.split()
    dict1={}
    for every_world in readlist:
        if every_world in dict1:
            dict1[every_world] += 1
        else:
            dict1[every_world] = 1
    return dict1
print(wordcount("you see see you , one day day"))