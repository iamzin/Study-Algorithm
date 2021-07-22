def solution(n):

    dp=[0 for _ in range(60001)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%1000000007

    answer=dp[n]
    return answer

print(solution(4))


import sys
sys.setrecursionlimit(60000)
def solution(n):
    
    dp=[0 for _ in range(60001)]
    dp[1]=1
    dp[2]=2
    def dfs(n):
        if dp[n]: 
            return dp[n]

        dp[n]=(dfs(n-1)+dfs(n-2))%1000000007
        return dp[n]


    answer=dfs(n)
    return answer