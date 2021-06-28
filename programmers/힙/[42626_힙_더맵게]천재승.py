import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    #모든 음식의 스코빌 지수가 K이상일 때까지 반복
    while scoville[0]<K: 

        #len(scoville)>1을 고려하지 않으면, 모든 테스트 중 1개가 틀리다.
        if len(scoville)>1:
            cnt+=1
            x=heapq.heappop(scoville)
            y=heapq.heappop(scoville)
            z=x+2*y
            heapq.heappush(scoville,z)
        
        else:
            return -1

    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))