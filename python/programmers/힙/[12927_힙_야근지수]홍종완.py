# 야근 지수 - 힙 - 12927
# 회사원 Demi는 가끔은 야근을 하는데요,
# 야근을 하면 야근 피로도가 쌓입니다.
# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
#
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,
# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

import heapq


def solution(n, works):
    answer = 0
    # test case 3번 - works의 원소의 합이 n보다 작을 경우엔 0
    # 야근 할 필요 없음
    if sum(works) < n:
        return 0

    # heap 만들것(max heap)
    # max heap을 만들때 튜플을 사용하고, 우선순위를 음수로 두어 최소 <-> 최대를 만들 수 있다
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))
    # print(works)
    # print(heap)

    cnt = 0
    while cnt < n:
        # a - 우선순위, b - 값
        a, b = heapq.heappop(heap)
        # 우선순위는 음수이므로 +1, 값은 -1
        heapq.heappush(heap, (a+1, b-1))
        cnt += 1

    # 값을 빼내기 위한 배열 생성
    temp = []
    for a, b in heap:
        temp.append(b)

    # 각 남은 값들의 제곱을 answer에 더한다
    for t in temp:
        answer += t**2

    return answer


print(solution(4, [4, 3, 3]))
