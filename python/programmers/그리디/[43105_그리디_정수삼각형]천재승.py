import copy
def solution(triangle):
    answer = 0

    dp=copy.deepcopy(triangle)
    for i in range(1,len(dp)): 
        for j in range(0,len(dp[i])): 
            if j==0: 
                dp[i][j]=dp[i-1][0]+dp[i][j]
            elif j==len(dp[i])-1:
                dp[i][j]=dp[i-1][j-1]+dp[i][j] 
            else: 
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+dp[i][j]
            
    
    print(dp)
    answer=max(dp[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))