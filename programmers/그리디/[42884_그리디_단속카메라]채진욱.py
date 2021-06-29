routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

# 범위
# 진입지점, 진출지점
# routes 반복문 돌면서
# min = -20
# max = -15
# min <= route <= max 라면 count += 1

# 진출지점에 카메라 달고
# route 돌면서
# 카메라에 찍히면 넘어가고
# 카메라에 안찍히면 안찍힌 route의 진출지점에 카메라 달기


def solution(routes):
    answer = 0
    camera_list = []

    out_list = sorted(routes, key=lambda x: x[1])
    camera_list.append(out_list[0][1])

    for i in range(len(out_list)):
        for j in range(len(camera_list)):
            if routes[i][0] <= camera_list[j] and routes[i][1] >= camera_list[j]:
                break
            else:
                if j == len(camera_list)-1:
                    camera_list.append(routes[i][1])

    print(camera_list)

    return len(camera_list)


# 참고 https://hbj0209.tistory.com/104
def solution2(routes):
    answer = 1

    # routes를 진출지점 순으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    # camera = 현재 카메라가 설치된 위치
    camera = routes[0][1]

    # 두 번째 차량부터 마지막 차량까지 반복문을 돌면서 현재 카메라가 설치된 시간보다
    # 차량 진입 시간이 늦으면 camera에 현재 차량의 진출시간을 넣어주고 answer 1 증가
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1

    return answer


print(solution2(routes))
