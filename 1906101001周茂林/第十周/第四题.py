'''
找到年龄最大的人，并输出。
字典“{"li":18,"wang":50,"zhang":20,"sun":22}”
'''
aa = {"li":8,"wang":50,"zhang":20,"sun":22}
bb = max(aa,key=aa.get)
print(bb)