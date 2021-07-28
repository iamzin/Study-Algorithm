from collections import deque

bridge_length = 100  # 다리에 올라올 수 있는 트럭 개수
# bridge_length는 결국 다리를 건너는데 필요한 시간
weight = 100  # 다리가 견딜 수 있는 중량
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # 대기 트럭 무게 리스트

# 대기하고 있는 트럭은 1초동안 하나씩 도로로 올라옴
# deque를 써서 다리를 지난 트럭은 popleft로
# 다리로 올라오는 트럭은 push로


def solution(bridge_length, weight, truck_weights):
    answer = 1  # 0초에서 1초되는 것도 count해야됨
    bridge_q = []  # 현재 도로에 있는 트럭 리스트
    left_time_list = []  # 현재 도로에 있는 트럭이 도로를 벗어나는데 까지 걸리는 시간 리스트
    complete_list = []  # 도로를 지난 트럭들을 담는 리스트
    truck_num = len(truck_weights)

    # 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
    # 1초가 지나야 트럭이 완전히 진입하므로 answer += 1, left_time_list에 추가
    bridge_q.append(truck_weights.pop(0))
    answer += 1
    left_time_list.append(bridge_length-1)

    print("bridge_q: ", bridge_q)
    print("left_time_list: ", left_time_list)

    while len(complete_list) != truck_num:
        if len(bridge_q) == 0:
            if len(truck_weights) > 0:  # 다리에 아무것도 없고 남은 트럭이 있을 때
                bridge_q.append(truck_weights.pop(0))
                left_time_list.append(bridge_length)
        else:  # 다리에 트럭이 있고
            if len(truck_weights) > 0:  # 남은 트럭이 있을때
                if sum(bridge_q) + truck_weights[0] <= weight and len(bridge_q) < bridge_length:
                    bridge_q.append(truck_weights.pop(0))
                    left_time_list.append(bridge_length)
        left_time_list = [x-1 for x in left_time_list]  # 밑에 주석 대신 한줄로 처리
        # for i in range(0, len(left_time_list)):
        #     left_time_list[i] -= 1
        if left_time_list[0] == 0:  # 맨 처음 시간이 0이라면
            left_time_list.pop(0)
            bridge_q.pop(0)
            complete_list.append("complete")
        answer += 1
        print("answer: ", answer)
        print("bridge_q", bridge_q)
        print("left_time_list", left_time_list)
        print("complete_list", complete_list)

    print("answer: ", answer)
    return answer


solution(bridge_length, weight, truck_weights)