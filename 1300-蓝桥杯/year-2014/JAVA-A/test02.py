'''
2.标题：李白打酒,
'''
import collections
def judge(res):
    x=2
    dic=collections.Counter(res)
    if dic["a"]==5 and dic["b"]==10:
        for i in res:
            if i=="b":
                x-=1
            elif i=="a":
                x*=2
        if x==0:
            print(res)
    else:
        pass

def re_track(track,i):
    if i>=15:
        judge(track)
        return
    track[i]="a"
    re_track(track,i+1)
    track[i]="b"
    re_track(track,i+1)


ls=[0]*15
re_track(ls,0)