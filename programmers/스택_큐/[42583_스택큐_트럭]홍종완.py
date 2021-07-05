# 다리를 지나는 트럭 - 스택/큐 - 42583
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
# 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
# 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length,
# 다리가 견딜 수 있는 무게 weight,
# 트럭 별 무게 truck_weights가 주어집니다.
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
from collections import deque

# 트럭이 다리를 건너는데 걸리는 시간은 bridge_length임, 1초에 1씩 이동


def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights = deque(truck_weights)
    # 다리 위에 있는 트럭들
    on_bridge = deque()
    # 다리 위에 있는 트럭들이 지나간 시간
    on_time = deque()

    # 트럭들이 모두 사라질 때까지(다리위, 트럭 리스트)
    while truck_weights or on_bridge:
        answer += 1
        # 다리위에 트럭이 있을때 시간
        if on_time:
            # 트럭이 다리 다 건넜으면
            if on_time[0] + bridge_length == answer:
                on_bridge.popleft()
                on_time.popleft()
        # 남은 트럭이 있으면
        if truck_weights:
            # 무게 조건
            if sum(on_bridge) + truck_weights[0] <= weight:
                # 다리위로 올림
                on_bridge.append(truck_weights.popleft())
                # 시간 증가
                on_time.append(answer)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
