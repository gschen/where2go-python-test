def count(n):
    sums=0
    cnt=0
    if n>13:
        return
    elif n==13:
        if sums==13:
            cnt+=1
    else:
        for i in range(0,5):
            sums+=i
            count(n+1)
            sums-=i
    return cnt
print(count(0))

# count=0
# for i in range(0,5):
#     for j in range(0,5):
#         for l in range(0, 5):
#             for m in range(0, 5):
#                 for n in range(0, 5):
#                     for o in range(0, 5):
#                         for p in range(0, 5):
#                             for q in range(0, 5):
#                                 for r in range(0, 5):
#                                     for s in range(0, 5):
#                                         for t in range(0, 5):
#                                             for u in range(0, 5):
#                                                 for v in range(0, 5):
#                                                     if i+j+l+m+n+o+p+q+r+s+t+u+v==13:
#                                                         count+=1
# print(count)


