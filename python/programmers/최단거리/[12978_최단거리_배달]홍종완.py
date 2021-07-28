# 배달 - bfs? - 12978

# N개의 마을로 이루어진 나라가 있습니다.
# 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다.
# 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데,
# 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다.
# 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
# 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.
import heapq


def solution(N, road, K):
    answer = []
    # 시작노드
    start = 1
    # 각 노드에
    graph = [[] for _ in range(N+1)]
    INF = int(1e9)
    distance = [INF] * (N + 1)

    # 간선 정보 기록
    for i in range(len(road)):
        a = road[i][0]
        b = road[i][1]
        c = road[i][2]
        graph[a].append((b, c))
        graph[b].append((a, c))
    # print(graph)

    q = []
    # 시작노드에서 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # print(q)
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # # 이미 처리된 적 있다면 무시
        # if distance[now] < dist:
        #     continue
        # 인접한 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # print(distance)
    for i in distance:
        if i <= K:
            answer.append(i)

    return len(answer)


road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
road2 = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
    3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]

print(solution(5, road, 3))
print(solution(6, road2, 4))
