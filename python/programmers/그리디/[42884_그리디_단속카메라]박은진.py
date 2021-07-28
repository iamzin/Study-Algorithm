# X : 그리디

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 나간 지점기준으로 정렬
    camera = -30001 # -30000이 기준이니까

    for route in routes:
        if camera < route[0]: # 차량 진입 지점보다 작은 지점에 카메라 있으면 +1
            answer += 1
            camera = route[1] # 나간 지점을 카메라 지점으로
    return answer