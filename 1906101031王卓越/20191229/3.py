import collections
arr=eval(input())
start=int(input())
dic=collections.defaultdict(int)
for num in range(len(arr)):
    dic[num]=0+arr[num]
s=[start]
while dic[start]==0:
    if dic[start+dic[start]]<=len(dic):
        start=dic[start+dic[start]]
        if start in s:
            print('False')
            break
        s.append(start)
    if dic[start-dic[start]]>=0:
        start=dic[start-dic[start]]
        if start in s:
            print('False')
            break
        s.append(start)
print('True')


