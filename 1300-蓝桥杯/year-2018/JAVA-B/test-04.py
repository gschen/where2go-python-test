# def test(phone,floor):
#     dp=[[]]
#     for i in range(1,phone+1):
#         for j in range(1,floor+1):
#             dp[i][j]=j
#     for i in range(2,phone+1):
#         for j in range(1,floor+1):
#             for k in range(1,j):
#                 dp[i][j]=min(dp[i][j],max(dp[i-1][k-1],dp[i][j-k])+1)
#     return dp
# print(test(3,1000))
dp=[[]]
inf = 0x3f3f3f3f
def test(n,m):
    dp=[[]]
    inf=0x3f3f3f3f
    if dp[n][m]!=inf:
        return dp[n][m]
    elif n==0:
        return dp[n][m]==0
    elif m==1:
        return dp[n][m]==n
    for i in range(1,n+1):
        dp[n][m]=min((dp[n][m],1+max(test(i-1,m-1)),test(n-i,m)))

    return dp[n][m]
for i in range(0,3):
    for j in range(0,1000):
        dp[i][j]=inf

print(test(3,1000))
