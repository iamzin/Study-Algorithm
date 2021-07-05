import heapq

jobs = [[0, 3], [1, 9], [2, 6]]
# 최소가 되려면
# 최대한 대기 시간을 줄이자
# 작은 작업 먼저 처리

# 요청되는 시점으로 sort하고
# 현재 시간부터 완료까지의 시간이 제일 짧은거 먼저 처리 (X)
# heapq를 사용해서 현재 시간부터 완료까지의 시간을 우선순위로 최소 힙 구현 (X)
# => 작업 소요 시간 기준으로 최소 힙 (O)
# 시간은 따로 처리 (O)
# 요청에서 종료까지 걸리는 시간 리스트 구성(X)


# 못 품
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))


solution(jobs)
