def solution(bridge_length, weight, truck_weights):

    # 빈 다리를 0으로 초기화
    # 컨테이너 벨트가 떠올랐다.
    trucks_on_bridge=[0]*bridge_length
    cur_time=0
    while trucks_on_bridge:

        cur_time+=1

        trucks_on_bridge.pop(0)
        
        if truck_weights:
            if sum(trucks_on_bridge)+truck_weights[0]<=weight:
                trucks_on_bridge.append(truck_weights.pop(0))

            else:
                trucks_on_bridge.append(0)

 
    answer=cur_time

    return answer


print(solution(2,	10,	[7,4,5,6]))