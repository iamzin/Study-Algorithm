import sys
sys.setrecursionlimit(60000) #재귀 호출을 늘려준다.
def solution(n):
    
    dp=[0 for _ in range(60001)]
    dp[1]=1
    dp[2]=2
    def dfs(n): #재귀 호출
        if dp[n]: 
            return dp[n]

        dp[n]=(dfs(n-1)+dfs(n-2))%1000000007
        return dp[n]


    answer=dfs(n)
    return answer

print(solution(4))