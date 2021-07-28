import heapq

def solution(priorities, location):
    answer = 0
    heap=[]

    #우선순위를 heapq에 넣는다.
    for priority in priorities:
        heapq.heappush(heap, -priority)
    

    while heap:
        for i in range(len(priorities)):
            
            #-heap[0]은 제일 높으 중요도를 의미한다.
            #현재 문서의 중요도가 -heap[0]와 같지 않음은 아직 대기목록에 현재 문서보다 중요도가 높은 문서가 존재함을 의미한다.
            #따로 else가 없는 이유는 어차피 할 일이 없다. 
            if priorities[i]==-heap[0]:
                
                answer+=1
                if i==location:
                    return answer
                #현재 문서가 제일 높은 중요도를 가지면 바로 인쇄한다.
                heapq.heappop(heap)
                
        





print(solution([1, 1, 9, 1, 1, 1],0))