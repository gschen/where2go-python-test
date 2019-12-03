# a=int(input())
# x=0
# A=[]
# while x<a:
#     s=list(map(float,input().split()))
#     x+=1
#     A.append(s)
# xiaolv=[]
# dic={}
# for i in range(0,a):
#     mins = 0
#     for j in range(0,len(A[0])):
#         y=A[i][j]*7
#         mins+=y
#     fina=A[i][-1]
#     xiao=mins/fina
#     xiaolv.append(xiao)
#     dic[i+1]=A[i][-1]
# print(xiaolv.index(max(xiaolv))+1,end=" ")
# print(int(dic.get(xiaolv.index(max(xiaolv))+1)))


N,K=map(int,input().split())
S=map(int,input().split())
list_1=list(S)
list_2=set(list_1)
list_3=list(list_2)
if len(list_3)<K:
    K=len(list_3)
print(list_3[0:K])







