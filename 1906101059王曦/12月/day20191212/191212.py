n=int(input())
li = list(range(1, n+1))
while len(li) > 3:
    del li[2]
    a, b = li[0], li[1]
    li.remove(a)
    li.remove(b)
    li.extend([a, b])
if 2 <= len(li) <= 3:
    print(li[1])
if len(li) == 1:
    print(li[0])