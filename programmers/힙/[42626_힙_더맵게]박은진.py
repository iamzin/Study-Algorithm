# X : heap

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer

# 종완님
# deque 는 재정렬에 시간 비효율
# 따라서 우선순위 있는 힙 사용