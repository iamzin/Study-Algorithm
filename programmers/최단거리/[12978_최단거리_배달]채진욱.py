import heapq
N = 6
road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
    3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
K = 4

INF = int(1e9)


def get_smallest_node(N, time, visited):
    min_value = INF
    index = 0
    for i in range(1, N+1):
        if time[i] < min_value and not visited[i]:
            min_value = time[i]
            index = i
    return index


def dijkstra(N, time, visited, graph):
    time[1] = 0
    visited[1] = True
    for j in graph[1]:
        time[j[0]] = j[1]

    for i in range(N-1):
        now = get_smallest_node(N, time, visited)
        visited[now] = True
        for j in graph[now]:
            cost = time[now] + j[1]
            if cost < time[j[0]]:
                time[j[0]] = cost


def dijkstra2(time, graph):  # 힙 사용했지만 정확성 70% -> 어디가 문제인지 모르겠음
    q = []

    heapq.heappush(q, (0, 1))
    time[0] = 0

    while q:
        dist, now = heapq.heappop(q)
        if time[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(N, road, K):

    graph = [[] for i in range(N+1)]  # graph 초기화
    visited = [False] * (N+1)  # 1번부터 인덱스 맞추기 위해 N+1로
    time = [INF] * (N+1)

    for i in range(len(road)):  # graph에 경로 정보 추가
        graph[road[i][0]].append([road[i][1], road[i][2]])
        graph[road[i][1]].append([road[i][0], road[i][2]])

    print(graph)

    dijkstra2(time, graph)
    answer = 0

    for i in range(1, N+1):
        if time[i] <= K:
            answer += 1
    return answer

# graph에 경로에 대한 정보를 넣어놓고
# visited라는 리스트에 마을에 다녀갔는지 확인하는 boolean 값을 설정
# 소요시간 값 리스트에 1번에서 해당 마을까지 걸리는 시간을 설정 (초기값은 무한대로 설정)
# 1번부터 시작해서 인접 노드에 방문하면서 걸린시간이 소요시간 리스트 값보다 적다면 소요시간 리스트 값을 갱신
#


def dijkstra3(start, road, distance):  # 참고한 코드 # https://greedysiru.tistory.com/492
    # 시작 마을에 대한 초기화(자기 자신은 거리가 0)
    distance[start] = 0
    # 큐에 삽입
    q = []
    heapq.heappush(q, (0, start))
    # 큐가 비어있지 않은 경우 계속 실행
    while q:
        # 가장 최단 거리가 짧은 마을 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 것이라면 무시
        if distance[now] < dist:
            continue
        # 거리 정보가 있는 road를 하나씩 접근
        for x in road:
            # 출발지가 현재 마을인 경우
            if x[0] == now:
                # 거쳐서 가는 비용
                cost = dist + x[2]
                # 거쳐서 간 다음 마을
                next = x[1]
                # 현재 마을을 거쳐서, 다른 마을로 이동하는 거리가 더 짧은 경우
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
            # 도착지가 현재 마을인 경우
            elif x[1] == now:
                cost = dist + x[2]
                # 현재 마을로 오기 위한 출발지
                prev = x[0]
                if cost < distance[prev]:
                    distance[prev] = cost
                    heapq.heappush(q, (cost, prev))
    return distance

# N: 마을의 수
# road: 도로의 정보가 쓰인 2차원 배열 각 요소의 인덱스는 [0]: 출발마을 [1]: 도착마을 [2]: 걸리는 시간
# 배달이 가능한 K이하의 시간


def solution2(N, road, K):
    answer = 0
    # 처음의 시작 마을 번호
    start = 1
    # 최단 거리 테이블을 무한으로 초기화
    distance = [int(1e9)] * (N + 1)
    # 다익스트라 알고리즘 실행
    dijkstra(start, road, distance)
    # 배달 거리가 K이하인 마을 갯수 구하기
    for x in distance:
        if x <= K:
            answer += 1
    return answer


print(solution2(N, road, K))
