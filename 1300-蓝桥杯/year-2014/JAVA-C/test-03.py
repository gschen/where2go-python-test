# s=106*['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
s=[1,2,3,4,5,6,7,8]
# x=[]
# def delete(s):
#     if len(s)==1:
#         return s
#     else:
#         for i in range(0,len(s),2):
#             print(i)
#             s.remove(s[i])
#         delete(s)
#     return s
# print(delete(s))
sum=0
for i in range(0,100):
    if pow(2,i)-2014>0:
        print(pow(2,i-1))
        sum+=pow(2,i-1)
        break

sum=sum%19
c=chr(97+sum-1)
print(c)





