def solution(n, times):
    answer = 0
    
    left=1 
    right=max(times)*n

    while(left<=right):
        #특정 시간
        mid=(left+right)//2
        cnt=0
        for time in times:
            cnt+=mid//time
        if cnt>=n:
            #cnt와 n이 같더라도 시간을 더 줄일 수 있는 경우가 생긴다. 예를 들어 mid가 29이면 cnt는6이 된다.
            answer=mid
            right=mid-1
            
        else:
            left=mid+1
            
    return answer