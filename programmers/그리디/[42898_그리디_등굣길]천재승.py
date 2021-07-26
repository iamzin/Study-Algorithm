def solution(m, n, puddles):
    #m: col, n: row
    answer= 0
    
    graph=[[0 for _ in range(m+1)] for _ in range(n+1)  ]

    #최단경로로 도착하려면 방향은 오른쪽 또는 아래만 이동 가능하다.
    
    graph[1][1]=1
    #puddles[0][0]: col, puddles[0][1]: row
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j, i] in puddles or (i,j)==(1,1): 
                continue
            
            graph[i][j]=(graph[i][j-1]+graph[i-1][j])%1000000007
            
    
    answer=graph[-1][-1]
    
    return answer