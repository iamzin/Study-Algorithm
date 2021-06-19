import heapq



def solution(N, road, K):
    answer = 0
    #무한을 의미하는 값으로 10억을 설정.
    INF=int(1e9)

    #최단거리 테이블 
    distance=[INF]*(N+1)

    #그래프
    graph=[[] for _ in range(N+1)]

    #그래프 채우기
    for a,b,c in road:
        graph[a].append((b,c))
        #이거 안해서 처음에 틀림
        graph[b].append((a,c))

    #다익스트라 함수 구현
    def dijksta(start): 
        q=[]
        distance[start]=0

        heapq.heappush(q, (0,start))

        while q:
            #우선순위 큐(heapq)를 쓰는 이유
            #방문하지 않는 노드 중 최단 거리가 가장 짧은 노드를 선택할 수 있다.
            dist, now= heapq.heappop(q)

            #현재 노드가 이미 처리된 적이있는 노드면 무시
            if distance[now] < dist:
                continue

            #현재 노드와 연결된 다른 인접한 노드들을 검사
            for next in graph[now]:
                cost= dist+next[1]
                #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우 갱신
                if cost < distance[next[0]]:
                    distance[next[0]]=cost
                    heapq.heappush(q,(cost, next[0]))

                
    dijksta(1)
    
    
    #K보다 작은 동네 찾기
    for i in range(1,N+1):
        if distance[i]<=K:
            # print(i, distance[i])
            answer+=1



    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))