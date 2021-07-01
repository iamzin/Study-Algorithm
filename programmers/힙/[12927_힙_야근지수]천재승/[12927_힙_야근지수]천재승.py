import heapq


def solution(n, works):
    
    
    #heapify
    #최대 작업량을 확인해야하므로 최대 힙 형태로 만든다. 
    works= [-work for work in works]
    heapq.heapify(works)
    
    for i in range(n):
        #최대 처리량 
        throughput=-heapq.heappop(works)

        #최대 처리량이 0이면 더 이상 감소할 일이 없으므로 break
        if throughput==0: 
            break

        #최대 처리량을 가진 일을 1만큼 처리
        heapq.heappush(works, -(throughput-1))

    
    return sum([work**2 for work in works])


print(solution(4, [4, 3, 3]))