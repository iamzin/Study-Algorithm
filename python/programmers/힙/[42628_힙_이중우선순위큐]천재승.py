import heapq

#힙을 1개가 아닌 2개를 만들어서 푼게 아쉽지만, 1개로 풀려면 heapq.nlargest(n, list) 사용해야 한다.
#heapq.nlargest(n, list) 함수를 사용하면 list에서 가장 큰 n개의 수를 뽑아낼 수 있다.
#heap = heapq.nlargest(len(heap), heap)[1:]
#heapq.heapify(heap)

def solution(operations):
    

    #최소힙
    heap=[]
    #최대힙
    max_heap= []

    for op in operations:
        print(op)
        #최소 제거
        if op=="D -1":
            if heap:
                n=heapq.heappop(heap)
                max_heap.remove(-n)
        #최대 제거
        elif op=="D 1":
            if max_heap:
                n=heapq.heappop(max_heap)
                heap.remove(-n)
        #삽입
        else:
            heapq.heappush(heap,int(op[2:]))
            heapq.heappush(max_heap,int(op[2:])*(-1))
    
    if heap:
        return [-max_heap[0], heap[0]] 

    else: 
        return [0,0]



print(solution(["I 7","I 5","I -5","D -1"]))