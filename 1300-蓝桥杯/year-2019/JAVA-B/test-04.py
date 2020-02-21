# count=0
# for i in range(1,2019):
#     if '2' in str(i) and '4'  in str(i) :
#         continue
#     for j in range(1,2019):
#         if '2'  in str(j) and '4'  in str(j):
#             continue
#         for k in range(1,2019):
#             if '2' in str(k) and '4'  in str(k):
#                 continue
#             if  i+j+k==2019:
#               count+=1
# print(count)
def panduan(n):
    while n>0:
        k=n%10
        if k==2 or k==4:
            return False
        n/=10
    return True

count=0

for i in range(1,2020):
    for j in range(1,2020):
        for k in range(1,2020):
            if i +j+k==2019:
                if i!=j and j!=k and i!=k :
                    if panduan(i) and panduan(j) and panduan(k):

                        count+=1
print(count)