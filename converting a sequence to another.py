def cost(s1,s2,dp,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    print(dp[-1][-1])
n=int(input())
s1=list(map(int,input().split()))
m=int(input())
s2=list(map(int,input().split()))
dp=[[0 for i in range(m+1)]for i in range(n+1)]
cost(s1,s2,dp,n,m)
