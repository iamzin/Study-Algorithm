def solution(board, moves):
    answer = 0
    bucket=[]
    #회전
    #0은 넣지 않는다.
    maps=[[] for _ in range(len(board))]
    for col in range(len(board)):
        for row in range(len(board)-1,-1,-1):
            if board[row][col]==0: 
                continue

            maps[col].append(board[row][col])
    
    #i번 찾아서 뽑는다.
    for i in range(len(moves)): 
        pos=moves[i]-1
        if len(maps[pos])>0:
            select=maps[pos][-1]
             
            maps[pos].pop()
                    
            #bucket의 top과 비교 
            #다르면 push
            if len(bucket)==0 or select!=bucket[-1]:    
                bucket.append(select)
            #같으면 pop and cnt+=2    
            else :
                bucket.pop()
                answer+=2

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))