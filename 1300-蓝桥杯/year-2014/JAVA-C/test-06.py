def dajiu(a,b,c,d):
    if a==0 or d==0:
        return 0
    elif a==1 and b==0 and c==0 and d==1:
        return 1
    return dajiu(a*2,b-1,c,d-1)+dajiu(a-1,b,c-1,d-1)
print(dajiu(2,5,9,15))
# a=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,2,2,2,2,2]
# for i in a:
#     for j in a:
#         for k in a:
#             for l in a:
#                 for m in a:
#                     for o in a:
#                         for p in a:
#                             for r in a:
#                                 for s in a:
#                                     for t in a:
#                                         for u in a:
#                                             for v in a:
#                                                 for w in a:
#                                                     for x in a:
#                                                         for y in a:
#                                                             if 2+i+j+k+l+m+o+p+r+s+t+u+v+w+x+y==0 and y==-1:
#                                                                 print(i,j,k,l,m,o,p,r,s,t,u,v,w,x,y)