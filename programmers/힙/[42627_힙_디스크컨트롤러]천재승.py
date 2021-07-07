#무조건 짧은 요청을 먼저 수행
import heapq
def solution(jobs):
    answer = 0
    wait = []
    last = -1
    now = 0
    count = 0
    lenth = len(jobs)
    while count < lenth:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(wait, job[1])
        if wait:
            answer += (len(wait) * wait[0])
            last = now
            now += heapq.heappop(wait)
            count += 1
        else:
            now += 1
    
    return answer//lenth